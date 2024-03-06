from geopy.geocoders import Nominatim
from haversine import haversine
import os
import numpy as np
import re

# 현재 경로
file_path = os.path.dirname(os.path.realpath(__file__))

def distance(info):
    address_list = []
    pattern = r'.*시.*구\s'
    for i in range(len(info)):
        if '주소' not in info[i]: # 주소 없는 경우 건너뛴다.
            continue
        addr = info[i]['주소']
        match = re.match(pattern, addr)
        if match:
            address_list.append(match.group(0))

    geolocoder = Nominatim(user_agent = 'South Korea', timeout=None)

    place_list = [] # 위도, 경도가 저장됨
    for address in address_list:
        geo = geolocoder.geocode(address)
        if geo is None:
            print(f"Cannot find coordinates for address: {address}")
            continue
        a = (geo.latitude, geo.longitude)
        place_list.append(a)

    home_address = open(str(file_path)+'\\home_address.txt', encoding='utf-8').read().strip()
    home = (geolocoder.geocode(home_address).latitude, geolocoder.geocode(home_address).longitude)

    distance = [] # 집과의 거리가 저장됨
    for place in place_list:
        distance.append(haversine(home, place))

    distance = np.array(distance)

    top5_distance = []
    for i in range(5): # 가까운 거리 순으로 5개 주소 가져온다.
        top5_distance.append(info[np.argsort(distance)[i]])
        
    return top5_distance