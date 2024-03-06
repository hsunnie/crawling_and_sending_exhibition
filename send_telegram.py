import requests
import os

# 현재 경로
file_path = os.path.dirname(os.path.realpath(__file__))

token = open(str(file_path) + '\\telegram_token.txt', 'r').read().strip()
chat_id = open(str(file_path) + '\\telegram_chatid.txt', 'r').read().strip()

def send_to_telegram(info):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    try:
        info_content = '<오늘 전시회 추천>\n\n'
        for i in range(5):
            for key in info[i]:
                if key=='전시회이미지':
                    continue
                info_content += key + ' : ' + info[i][key] + '\n'
            info_content += '\n'
        res = requests.post(url, json={'chat_id': chat_id, 'text':info_content})

    except Exception as e:
        print(e)