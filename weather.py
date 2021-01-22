from bs4 import BeautifulSoup
from pprint import pprint
import requests

def number(N):
    final = ""
    for i in N:
        try:
            final += str(int(i))
        except ValueError:
            pass
    return final

def weather(time):
    html = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=0&acr=1&acq=%EB%82%A0%EC%94%A8&qdt=0&ie=utf8&query=%EB%82%A0%EC%94%A8")
    soup = BeautifulSoup(html.text, 'html.parser')
    cut = soup.find("div",{"class":"weather_box"})
    if time == '오늘':
        cut1 = cut.find("div",{"class":"today_area"})
        cut2 = cut1.find("dl",{"class":"indicator"})
        data = cut2.findAll("dd")
        data1 = cut2.findAll("dt")
        data2 = cut1.find("span",{"class":"merge"}).text.split('/')
        finaldata = '오늘 온도는 ' + cut1.find("span",{"class":"todaytemp"}).text + '도로 최고 온도 '+data2[1] + ' 최저 온도 ' + data2[0] + '이고 ' + cut1.find("p",{"class":"cast_txt"}).text
        for i in range(len(data)):
            finaldata += data1[i].text + '는 ' + number(data[i].text)
        return finaldata+' 입니다.'
    elif time == '내일':
        check = cut.find("div",{"class":"tomorrow_area _mainTabContent"})
        test = check.findAll('div',{'class':'main_info morning_box'})
        check1 = test[1].text.split()
        check2 = test[0].text.split()
        finaldata = '내일 오전 온도는 ' + number(check2[1]) + '도이고 ' + check2[2] + check2[3] + '는 ' + check2[4]+'입니다. 그리고 오후 온도는 '+number(check1[1])+'도이고 '+check1[2] + check1[3] + '는 '+check1[4]+' 입니다'
        return finaldata
    elif time == '모레':
        ok = cut.find("div",{"class":"tomorrow_area day_after _mainTabContent"})
        test1 = ok.findAll('div',{'class':'main_info morning_box'})
        ok1 = test1[1].text.split()
        ok2 = test[0].text.split()
        finaldata = '내일 오전 온도는 ' + number(ok2[1]) + '도이고 ' + ok2[2] + ok2[3] + '는 ' + ok2[4]+'입니다. 그리고 오후 온도는 '+number(ok1[1])+'도이고 '+ok1[2] + ok1[3] + '는 '+ok1[4]+' 입니다'
        return finaldata
