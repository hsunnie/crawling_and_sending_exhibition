import pymysql
import os

# 현재 경로
file_path = os.path.dirname(os.path.realpath(__file__))


def database_connect(info):
    # 데이터베이스 연결
    db_info = []
    for i in range(5):
        db_info = open(str(file_path)+'\\secret.txt').read().split('\n')
    conn = pymysql.connect(
        host=db_info[0], # 어떤 컴퓨터에 있는 데이터베이스에 접속할 것인지 설정
        user=db_info[1], # 사용자 계정
        password=db_info[2], # 비밀번호가 적힌 파일에서 비밀번호 읽어옴
        database=db_info[3], # 사용할 데이터베이스 선택
        charset=db_info[4]
    )

    # 테이블 생성 (crawling 테이블이 없는 경우에만 생성되도록함)
    with conn.cursor() as cursor:
        sql = """CREATE TABLE IF NOT EXISTS crawling (
                전시이름 varchar(150),
                장소 varchar(150),
                주소 varchar(150),
                기간 varchar(150),
                시간 varchar(150),
                대상 varchar(32),
                요금 varchar(32),
                상세페이지 varchar(200),
                전시회이미지 varchar(300),
                PRIMARY KEY(전시이름)
                );"""
        cursor.execute(sql)

        # 데이터 삽입
        for row in info:
            # 전시 이름이 존재하지 않는 경우에만 데이터 삽입
            columns = ', '.join(row.keys())
            placeholders = ', '.join(['%s'] * len(row))
            # Adjusted the SQL query string
            insert_sql = f"INSERT IGNORE INTO crawling ({columns}) VALUES ({placeholders});"
            cursor.execute(insert_sql, tuple(row.values()))

    # # 데이터 조회 (SELECT)
    # with conn.cursor() as cursor:
    #     sql = """SELECT * FROM crawling;"""
    #     cursor.execute(sql)
    #     x = cursor.fetchall()
    # print(x)

    conn.commit()
    conn.close()