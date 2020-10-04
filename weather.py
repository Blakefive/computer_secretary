from bs4 import BeautifulSoup
from pprint import pprint
import requests

def weather():
    html = requests.get('https://search.naver.com/search.naver?query=날씨')
    soup = BeautifulSoup(html.text, 'html.parser')
    data1 = soup.find('div', {'class': 'weather_box'})
    find_address = data1.find('span', {'class':'btn_select'}).text
    find_currenttemp = data1.find('span',{'class': 'todaytemp'}).text

    data2 = data1.findAll('dd')
    find_dust = data2[0].find('span', {'class':'num'}).text
    find_ultra_dust = data2[1].find('span', {'class':'num'}).text
    find_ozone = data2[2].find('span', {'class':'num'}).text
    test = data1.find('span',{'class' : 'merge'}).text
    test1 = data1.find('span',{'class' : 'sensible'}).text
    e = ''
    r = ''
    check = 0
    for i in range(len(test)):
        if check == 0:
            if test[i] == '/':
                check = 1
            try:
                e += str(int(test[i]))
            except:
                pass
        elif check == 1:
            try:
                r += str(int(test[i]))
            except:
                pass
    
    return '현재 위치는 ' + find_address + '으로' + '최저 온도' + e +'도, 최고 온도' + r+ '도, 현재 온도' + find_currenttemp + '도 입니다' + '그리고 미세먼지'+find_dust+'초미세먼지'+find_ultra_dust+'오존 지수' + find_ozone+'입니다'
