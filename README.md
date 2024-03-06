# exhibition_crawling_and_sending

- 프로젝트 기간 : 2024.02.22 ~ 2024.03.06

- 주제 : 오늘 전시 알아보기 (서울 문화 포털 - 전시)

- 대상 사이트 : https://culture.seoul.go.kr/culture/culture/cultureEvent/list.do?searchCate=EXHIBITION&menuNo=200009

- 프로그램 진행 과정
	1. 현재 날짜를 기준으로 전시 정보를 크롤링한다.
	2. 크롤링한 데이터 중 데이터베이스에 저장되지 않은 항목만 데이터베이스에 저장한다.
	3. 크롤링 결과를 이메일로 보낸다.
	4. 크롤링한 결과를 html 파일로 생성하여 보여준다.
	5. 집 주소 파일이 있는 경우, 거리를 계산하여 가까운 곳 top5를 텔레그램으로 전송한다.

- 파일 정보
	1. main.py : 아래 다섯 개의 파일로부터 함수를 가져와 크롤링
    -> 데이터베이스 저장, 이메일 발송, html 파일 생성, 거리계산, 텔레그램 발송을 할 수 있도록 전처리 과정을 담고 있는 파일
	2. exhibition_crawl.py : 오늘 날짜 기준으로 서울 문화 포털의 전시 정보를 크롤링할 수 있는 함수가 담긴 파일.
    -> 전시이름/장소/주소/기간/시간/대상/요금/상세페이지/전시회이미지 크롤링
	3. database_upload.py : 크롤링한 데이터를 가져와 데이터베이스에 동일한 전시이름이 없다면, 데이터베이스에 추가하는 함수가 담긴 파일
    -> 데이터베이스 정보가 담긴 파일을 필요로 하며, 데이터베이스 이름은 crawling이다.
	4. send_email.py : 크롤링한 데이터를 가져와 이메일을 보낼 수 있는 함수를 포함한 파일.
    -> 네이버아이디 및 비밀번호 파일 필요
	5. distance_calculation.py : 크롤링한 데이터의 주소 정보를 통해 집 주소와의 거리를 측정
    -> 집주소 파일 필요
	6. send_telegram.py : 집과 거리가 가까운 5개의 전시회를 텔레그램으로 전송하는 파일
    -> 텔레그램 chatid 및 token 파일 필요
    -> 집주소가 있는 경우에만 작동
	7. requirements.txt : 파일 실행에 필요한 라이브러리의 목록

- 추가로 필요한 정보
	- 네이버 아이디(naverid.txt)
	- 네이버 비밀번호(naverpw.txt)
	- 데이터베이스 정보(secret.txt)
		- 반드시 순서와 같이 작성하며, 각 요소는 줄바꿈으로 구분된다. (host, user, password, database, charset)
	- 집 주소(home_address.txt)
	- 텔레그램 chatid(telegram_chatid.txt)
	- 텔레그램 token(telegram_token.txt)

- 프로그램 실행
  1. 해당 파일은 PyMySQL을 활용하여 데이터베이스에 크롤링 데이터를 저장하므로 사전에 MySQL 및 MariaDB의 설치가 필요하다.
  2. 파일을 모두 다운로드 한다. (하나의 폴더에 저장)
  3. 동일한 폴더에 추가로 필요한 정보를 담은 파일을 생성한다.
  4. requirements.txt의 라이브러리를 설치한다.
  5. main.py 파일을 실행한다.
