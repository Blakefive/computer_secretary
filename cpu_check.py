import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def call(html,gg):
    while True:
        try:
            html1 = requests.get(html[gg])
            soup = BeautifulSoup(html1.content,'html.parser')
            data = soup.find('div',{'class':'left-desc-cpu'})
            final = go(str(data.get_text()).split())
            data = call2(soup)
            return final, data
        except AttributeError:
            if len(html)-1 >= gg:
                gg += 1
                call(html,gg)
def call2(soup):
    data = str(soup.select('div.right-desc > span'))
    data = ok2(data)
    return data
def go(checklist):
    test = 8
    check = []
    for i in checklist:
        qq = ''
        if i == 'Description:' or i == 'Class:' or i == 'Socket:' or i == 'Clockspeed:' or i == 'Speed:' or i == 'Cores:' or i == 'Threads:' or i == 'Down:' or i == 'TDP:' or i =='TDP' or i == 'Typical' or i == 'Up:' or i == 'Turbo':
            test += 1
        else:
            try:
                check[test-1] += (" " +i+qq)
            except IndexError :
                check.append((" " +i+qq))
    check = clean(check)
    return check

def clean(text):
    final_str = ""
    for i in range(len(text)):
        for j in range(len(text[i])):
            if text[i][j:] != "Class:":
                final_str += text[i][j]
            elif text[i][j:] == "Class:":
                break
        text[i] = final_str
        final_str = ""
    text = ok(text)
    return text

def ok(final):
	gg = 0
	totall = []
	ll = ''
	if final[0] == ' Intel':
		ll += final[0] + " "+final[1] + " " + final[2] + " " + final[3]
		gg = 4
	elif final[0] == ' with':
		ll += final[0] + ' ' + final[1] + ' '+ final[2]
		gg = 3
	totall.append(ll)
	oo = ''
	test = 0
	for i in range(gg,len(final)-1):
		    if final[i] == ' Turbo':
			    oo += final[i]
			    totall.append(oo)
			    oo = ''
		    elif ((final[i+1] == ' GHz' or final[i+1] == ' W' or final[i+1] == 'W3' or final[i+1] == ' Turbo') and (final[i] != ' GHz' and final[i] != ' W' and final[i] != 'W3' and final[i] != ' Turbo')) or (final[i+1] == ' Turbo') :
			    oo += final[i]
		    elif final[i] != ' GHz' and final[i] != ' W' and final[i] != 'W3':
			    totall.append(final[i])
		    elif (final[i] == ' GHz' or final[i] == ' W' or final[i] == 'W3') and final[i+1] != ' Turbo' :
			    oo += final[i]
			    totall.append(oo)
			    oo = ''
	totall.append(final[len(final)-2] + final[len(final)-1])
	return totall

def ok2(data):
	test =0
	final = ''
	for i in range(len(data)):
		if test == 0:
			if data[i] == '>':
				test = 1
		elif test == 1:
			if data[i] == '<':
				return final
			else:
				final += data[i]
def main(N):
    Nlist = N.split()
    M = "-".join(Nlist)
    html = "https://www.passmark.com/search/zoomsearch.php?zoom_sort=0&zoom_xml=0&zoom_per_page=10&zoom_and=1&zoom_cat%5B%5D=-1&zoom_query="
    html += M
    html = requests.get(html)
    soup = BeautifulSoup(html.content,'html.parser')
    test = str(soup.findAll('div',{'class':'result_title'})).split('<a')
    data1, data2 = split_data(test)
    return str('벤치마크 점수는 ' + data2 + '이고 ' + data1[0] + '에서 만들었으며 ' + data1[1] + ' 모델로 만들어졌습니다. 그리고'+ data1[2] +' 소켓이고 터보 클럭 '  + data1[3] + '기본 클럭' + data1[4] +'이며 ' + data1[5] + '코어' + data1[6] +'스레드입니다.' + ' 그리고 기본 열 설계 전력는 ' + data1[len(data1)-1] + '입니다')
    
def split_data(test):
    dd = []
    result = []
    final = []
    final_result = []
    for i in range(len(test)):
        for j in range(len(test[i].split('a>'))):
            dd.append(test[i].split('a>')[j])
    for i in range(len(dd)):
        if 'href' in dd[i]:
            result.append(dd[i])
    for i in range(len(result)):
        if 'Price performance comparison' in result[i]:
            final.append(result[i])
    for i in range(len(final)):
        oo = ''
        check = 0
        for j in range(len(final[i])):
            if check == 0:
                if final[i][j] == '"':
                    check = 1
            elif check == 1:
                if final[i][j] == '"':
                    final_result.append(oo)
                    break
                oo += final[i][j]
    if len(final_result) != 0:
        data1, data2 = call(final_result,0)
        return data1, data2
    elif len(final_result) < 1:
        return '',''
