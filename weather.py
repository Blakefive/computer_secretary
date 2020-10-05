from bs4 import BeautifulSoup
from pprint import pprint
import requests

def weather(time):
    html = requests.get('https://search.naver.com/search.naver?query=내일 날씨')
    soup = BeautifulSoup(html.text, 'html.parser')
    data1 = soup.find('div', {'class': 'weather_box'})
    find_address = data1.find('span', {'class':'btn_select'}).text
    find_currenttemp = data1.find('span',{'class': 'todaytemp'}).text
    data2 = data1.findAll('dd',{'class' : 'lv2'})
    test = data1.find('span',{'class' : 'merge'}).text
    e1 = data1.findAll('span',{'class':'todaytemp'})
    t = data1.findAll('span',{'class':'lv1'})
    r1 = data1.findAll('p',{'class':'cast_txt'})
    p1 = data1.findAll('span',{'class':'lv2'})
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
    if time == '오늘':
        return '현재 위치는 ' + find_address + '입니다...' +r1[0].text + '최저 온도' + e +'도, 최고 온도' + r+ '도, 현재 온도' + find_currenttemp + '도 입니다' + ' 그리고 미세먼지는 '+str(data2[0].text)[-2:]+' 초미세먼지는 '+str(data2[0].text)[-2:]+' 입니다'
    if time == '내일':
        return '현재 위치는 ' + find_address + '입니다... 오전에는 ' + r1[1].text + '이고 오후는 ' + r1[2].text + '입니다.' + '오전 온도는 ' + e1[1].text + '도. 오후 온도는 ' + e1[2].text + '도 입니다 그리고 오전 미세먼지는' +t[0].text +'오후 미세먼지는' + t[1].text + '입니다'
    if time == '모레':
        return '현재 위치는 ' + find_address + '입니다... 오전에는 ' + r1[3].text + '이고 오후는 ' + r1[4].text + '입니다.' + '오전 온도는 ' +e1[3].text + '도. 오후 온도는 ' + e1[4].text + '도 입니다 그리고 오전 미세먼지는'+p1[1].text +'오후 미세먼지는' + p1[2].text + '입니다'
