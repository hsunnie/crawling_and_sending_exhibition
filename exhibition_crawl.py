import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

def exhibition_crawl():
    date = str(datetime.now().strftime('%Y %m %d').replace(' ', "-"))
    menuNo = 200009
    URL = 'https://culture.seoul.go.kr/culture/culture/cultureEvent/culturalEventCalendarList.json'
    response = requests.post(URL, data={
    'pageIndex': 1, 
    'menuNo': 200009, 
    'searchCost': 0, 
    'searchField': 'EXHIBITION', 
    'sdate': {date}, 
    'edate': {date}, 
    'field': 'EXHIBITION', 
    'time': 'on'
    })

    python_data = json.loads(response.text)

    base_url = 'https://culture.seoul.go.kr'

    exh_list = []
    for i in range(len(python_data['calendarList'])):
        exh_dict = {}
        exh_dict['전시이름'] = python_data['calendarList'][i]['title']
        cultcode = python_data['calendarList'][i]['cultcode']
        detail_URL = f'https://culture.seoul.go.kr/culture/culture/cultureEvent/view.do?cultcode={cultcode}&menuNo={menuNo}'
        
        detail_response = requests.get(detail_URL)
        soup = BeautifulSoup(detail_response.text, 'html.parser')

        exh_dict['장소'] = soup.select_one('li:nth-child(1) > div.type-td').text.strip()
        
        if python_data['calendarList'][i]['addr'] is not None:
            exh_dict['주소'] = python_data['calendarList'][i]['addr']
        exh_dict['기간'] = python_data['calendarList'][i]['strtdate'] + ' ~ ' + python_data['calendarList'][i]['endDate']


        exh_dict['시간'] = soup.select_one('li:nth-child(3) > div.type-td').text.strip()
        exh_dict['대상'] = soup.select_one('li:nth-child(4) > div.type-td').text.strip()
        exh_dict['요금'] = soup.select_one('li:nth-child(5) > div.type-td').text.strip()
        
        exh_dict['상세페이지'] = detail_URL
        
        img = soup.select_one('div.intro-top.clearfix > div.img-box > img').attrs['src']
        img_url = base_url + img
        exh_dict['전시회이미지'] = img_url

        exh_list.append(exh_dict)
    
    return exh_list, date