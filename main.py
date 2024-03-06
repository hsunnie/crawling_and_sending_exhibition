from exhibition_crawl import exhibition_crawl
from database_upload import database_connect
from send_email import send_email
import webbrowser
from distance_calculation import distance
from send_telegram import send_to_telegram
import os

# 현재 경로
file_path = os.path.dirname(os.path.realpath(__file__))


# 현재 날짜 기준으로 크롤링
print('크롤링 시작! 잠시만 기다려주세요.')
info, date = exhibition_crawl()
print(f'-> {date[:4]}년 {date[5:7]}월 {date[8:10]}일 전시정보 크롤링 완료')

# 데이터베이스에 저장
database_connect(info)
print('-> 데이터베이스 저장 완료')

# 크롤링 데이터 전처리 (html 파일 형식으로 변환)
title = f'오늘({date[:4]}년 {date[5:7]}월 {date[8:10]}일) 서울 전시회 정보'
info_str = f'<h2>{date[:4]}년 {date[5:7]}월 {date[8:10]}일 전시회 목록</h2>\n<hr>\n'
for i in range(len(info)):
    info_str += '<table border:"1px solid black">\n'
    for key in info[i].keys():
        if key == '전시회이미지':
            info_str += ' <tr>\n<td>전시회이미지</td>\n<td><A href="'+ info[i][key] +'"><img src=" ' + info[i][key] + ' " height="500px"></img></A></td>\n</tr>\n '
        elif key == '상세페이지':
            info_str += '<tr>\n' + '<td>' + key + ' </td>\n' + '<td><A href="'+ info[i][key] + '">' + info[i][key]+ ' </A></td>\n' + ' </tr>\n'
        else:
            info_str += '<tr>\n' + '<td>' + key + ' </td>\n' + '<td>' + info[i][key]+ ' </td>\n' + ' </tr>\n'
    info_str += '</table>\n<hr>\n'


# 이메일 보내기
# answer = input('크롤링 정보를 이메일로 보내시겠습니까? yes or no : ')
# if answer=='yes' or answer=='YES':
#     send_email(title, info_str)
#     print('-> 이메일 발송 완료')
# else:
#     print('-> 이메일을 발송하지 않고 다음 단계로 넘어갑니다.')
send_email(title, info_str)
print('-> 이메일 발송 완료')


# html 파일 생성하기
head = """<!DOCTYPE html><html><head>
                    <style>
                        table, td, th {
                        border: 1px solid black;
                        }
                        
                        table {
                        border-collapse: collapse;
                        width: 100%;
                        }
                        
                        td {
                        padding: 1px 10px;
                        }
                    </style></head><body>"""
tail = """</body></html>"""
content = head + info_str + tail

file_name = file_path + f'\\{date}.html'
with open(file_name, 'w') as f:
    f.write(content)
    f.close()

webbrowser.open_new_tab(file_name) # html 파일 열기

# 거리 계산
if 'home_address.txt' in os.listdir(file_path):
    print('집과의 거리를 계산중입니다.')
    h = distance(info)

    # # 출력 (거리 가까운 순서 top 5)
    # distance_content = ''
    # for i in range(5):
    #     for key in h[i]:
    #         distance_content += key + ' : ' + h[i][key] + '\n'
    #     distance_content += '\n'
    # print(distance_content)

    # 텔레그램 발송
    print('가까운 거리에서 진행중인 전시회 5개를 텔레그램으로 발송합니다.')
    send_to_telegram(info)
    print('-> 텔레그램 발송완료')
