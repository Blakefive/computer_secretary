import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import psutil
import webbrowser
import pyautogui
import time
from selenium import webdriver
from googletrans import Translator
import youtube
import platform
from PIL import Image
import subprocess
import clipboard
import threading
import main
from selenium.webdriver.common.keys import Keys

def name(text):
    hh = 0
    pp = 0
    go = ""
    rr = ""
    for i in range(len(text.split())):
        if hh == 0:
            if '찾아' in text.split()[i] or '틀어' in text.split()[i] or '검색' in text.split()[i] or '켜' in text.split()[i]:
                hh = 1
            elif pp == 0 and not( '새' in text.split()[i] or  '세' in text.split()[i] or '창' in text.split()[i]) and not '대해' in text.split()[i]:
                go = go + text.split()[i]
                pp = 1
            elif pp == 1 and not( '새' in text.split()[i] or  '세' in text.split()[i] or '창' in text.split()[i]) and not '대해' in text.split()[i]:
                go = go + " " + text.split()[i]
    return go

def name1(text):
    hh = 0
    pp = 0
    go = ""
    rr = ""
    check = 0
    if '영어' in text.split()[0]:
        check = 1
    for i in range(len(text.split())):
        if hh == 0:
            if '찾아' in text.split()[i] or '틀어' in text.split()[i] or '재생' in text.split()[i] or '켜' in text.split()[i] or '검색' in text.split()[i]:
                hh = 1
            elif pp == 0 and not '유튜브' in text.split()[i] and not '대해' in text.split()[i]:
                go = go + text.split()[i]
                pp = 1
            elif pp == 1 and not '유튜브' in text.split()[i] and not '대해' in text.split()[i]:
                go = go + " " + text.split()[i]
    if check == 1:
        translator = Translator()
        result = translator.translate(go, dest="en")
        go = result,text
    return go
def run(N):
    if N == 1:
        subprocess.run('notepad')
    if N == 2:
        os.system('calc')
def speak(text,check):
    if check == 7:
        tts = gTTS(text=text, lang='ko')
        filename = 'music/data.mp3'
        tts.save(filename)
        playsound.playsound(filename)
        os.remove('music/data.mp3')
    if check == 6:
        pyautogui.hotkey('ctrl','up')
        tts = gTTS(text=text, lang='ko')
        filename = 'music/data.mp3'
        tts.save(filename)
        playsound.playsound(filename)
        os.remove('music/data.mp3')
    if check == 5:
        pyautogui.hotkey('ctrl','down')
        tts = gTTS(text=text, lang='ko')
        filename = 'music/data.mp3'
        tts.save(filename)
        playsound.playsound(filename)
        os.remove('music/data.mp3')
    if check == 3:
        tts = gTTS(text=text, lang='ko')
        filename = 'music/data.mp3'
        tts.save(filename)
        playsound.playsound(filename)
        os.remove('music/data.mp3')
    if check == 1:
        webbrowser.open("https://www.google.com/search?q="+text)
        tts = gTTS(text=text+"를 찾습니다", lang='ko')
        filename = 'music/data.mp3'
        tts.save(filename)
        playsound.playsound(filename)
        os.remove('music/data.mp3')
    if check == 2:
        webbrowser.open_new("https://www.google.com/search?q="+text)
        tts = gTTS(text="새 창으로 " + text+"를 찾습니다", lang='ko')
        filename = 'music/data.mp3'
        tts.save(filename)
        playsound.playsound(filename)
        os.remove('music/data.mp3')
    if check == 0:
        tts = gTTS(text=text, lang='ko')
        filename = 'music/data.mp3'
        tts.save(filename)
        playsound.playsound(filename)
        os.remove('music/data.mp3')
    print(text)
def ok(data):
    if '예' in data:
        main.do(0)
def check(N,hh,driver):
    if N == None:
        main.do(1)
        return 1,hh,driver
    if '아니' in N or '다시' in N or '아 맞다' in N or '됐어' in N:
        playsound.playsound('music/cancel.mp3')
        speak('나중에 다시 불러주세요',0)
        return 1,hh,driver
    elif '붙여' in N and ('놓기' in N or '넣기' in N):
        speak(str(clipboard.paste()) + ' 을 붙여놓겠습니다',0)
        pyautogui.write(clipboard.paste())
        print(clipboard.paste())
        return 1,hh,driver
    elif '계산기' in N and ('실행' in N or '켜' in N or '틀어' in N or '열어' in N):
        playsound.playsound('music/open program.wav')
        speak('계산기를 실행시킵니다',0)
        t2 = threading.Thread(target=run, args=(2, ))
        t2.start()
        return 1,hh,driver
    elif '계산기' in N and ('꺼' in N or '종료' in N or '멈춰' in N):
        speak('계산기를 끕니다.',0)
        playsound.playsound('music/click.mp3')
        os.system('taskkill.exe /f /im calculator.exe')
        return 1,hh,driver
    elif '메모장' in N and('실핼' in N or '켜' in N or '틀어' in N or '열어' in N):
        playsound.playsound('music/open program.wav')
        speak('메모장을 실행시킵니다',0)
        t1 = threading.Thread(target=run, args=(1, ))
        t1.start()
        return 1,hh,driver
    elif '메모장' in N and('꺼' in N or '종료' in N or '멈춰' in N):
        speak('메모장을 끕니다.',0)
        playsound.playsound('music/click.mp3')
        os.system('taskkill.exe /f /im notepad.exe')
        return 1,hh,driver
    elif '날짜' in N:
        tm = time.localtime() 
        speak(str(tm.tm_year)+"년 "+str(tm.tm_mon)+"월 "+str(tm.tm_mday)+"입 입니다",0)
        return 1,hh,driver
    elif '시간' in N:
        tm = time.localtime() 
        speak(str(tm.tm_hour)+"시 "+str(tm.tm_min)+"분 "+str(tm.tm_sec)+"초 입니다",0)
        return 1,hh,driver
    elif ('스크린샷' in N or '캡처' in N or '스샷' in N) and ('보여' in N or '확인' in N or '체크' in N):
        speak('스크린샷한 것을 보여드립니다.',0)
        im = Image.open('image/imagedata.png')
        im.show()
        return 1,hh,driver
    elif ('스크린샷' in N and '찍어' in N) or '스샷' in N or '캡처' in N:
        speak('스크린샷을 찍습니다,',0)
        playsound.playsound('music/camera.mp3')
        pyautogui.screenshot('image/imagedata.png')
        return 1,hh,driver
    elif '컴퓨터' in N  and ('확인' in N or  '체크' in Ns) :
        speak('cpu을 '+str(psutil.cpu_percent())+'퍼센트 사용 중입니다'+' 그리고 메모리는 '+str(psutil.virtual_memory().percent)+ '퍼센트 사용 중입니다',0)
        return 1,hh,driver
    elif ('다음' in N or '앞' in N or '다시' in N) and ('영상' in N) and ('찾아' in N or '틀어' in N or '켜' in N):
        speak('다음 영상을 재생합니다',0)
        element = driver.find_element_by_id('movie_player')
        element.send_keys(Keys.SHIFT,"n")
        return 1,hh,driver
    elif ('다음' in N or '앞' in N or '다시' in N):
        speak('앞으로 갑니다',0)
        driver.forward()
        return 1,hh,driver
    elif ('이전' in N or '그전' in N or '뒤' in N):
        speak('이전 영상을 재생합니다',0)
        driver.back()
        return 1,hh,driver
    elif ('찾아' in N or '검색' in N) and '유튜브' in N:
        if hh == 0:
            driver = webdriver.Chrome('chromedriver.exe')
        playsound.playsound('music/insert.wav')
        youtube.getTitles(name1(N),driver,1)
        return 1,1,driver
    elif '제목' in N and ('재생' in N or '틀어' in N or '켜' in N) and '유튜브' in N:
        if hh == 0:
            driver = webdriver.Chrome('chromedriver.exe')
        playsound.playsound('music/insert.wav')
        youtube.getTitles(name1(N),driver,0)
        return 1,1,driver
    elif ('재생' in N or '틀어' in N or '켜' in N) and '유튜브' in N:
        if hh == 0:
            driver = webdriver.Chrome('chromedriver.exe')
        playsound.playsound('music/insert.wav')
        youtube.getTitles(name1(N),driver,2)
        return 1,1,driver
    elif ('찾아' in N or '틀어' in N or '켜' in N or '검색' in N) and ('새창' in N or '새 창' in N or '세 창' in N or '세창' in N):
        playsound.playsound('music/insert.wav')
        speak(name(N),2)
        return 1,hh,driver
    elif '찾아' in N or '틀어' in N or '켜' in N or '검색' in N:
        playsound.playsound('music/insert.wav')
        speak(name(N),1)
        return 1,hh,driver
    elif ('음악' in N or '노래' in N or '소리' in N) and  ('줄여' in N  or '내려' in N):
        speak('소리를 줄입니다',5)
        return 1,hh,driver
    elif ('음악' in N or '노래' in N or '소리' in N) and  ('올려' in N or '키워' in N) :
        speak('소리를 올립니다',6)
        return 1,hh,driver
    elif ('화면' in N or '모니터' in N )and '밝기' in N and ('올려' in N or '키워' in N) :
        speak('화면 밝기를 올립니다',7)
        pyautogui.hotkey('ctrl','shift','fn','alt','o')
        return 1,hh,driver
    elif ('화면' in N or '모니터' in N) and '밝기' in N and ('줄여' in N or '내려' in N) :
        speak('화면 밝기를 줄입니다',7)
        pyautogui.hotkey('ctrl','shift','fn','alt','p')
        return 1,hh,driver
    elif '컴퓨터' in N and ('bit' in N or '비트' in N) and ('알려' in N or '뭐' in N or '확인' in N or '체크' in N):
        speak(str(platform.machine())[3:] + '.비트 입니다',0)
        return 1,hh,driver
    elif '컴퓨터' in N and ('os' in N or '운영체제' in N or 'operating system' in N) and ('확인' in N or '알려' in N or '뭐' in N or '확인' in N):
        speak(str(platform.system()),0)
        return 1,hh,driver
    elif '컴퓨터' in N and ('cpu' in N or '중앙처리장치' in N) and '코어' in N and '수' in N and ('확인' in N or '알려' in N or '뭐' in N or '확인' in N):
        speak(str(psutil.cpu_count(logical=False)),0)
        return 1,hh,driver
    elif '노래' in N and ('멈춰' in N or '꺼' in N):
        speak('넵 노래를 멈추겠습니다.',0)
        playsound.playsound('music/remove.wav')
        driver.quit()
        return 1,0,driver
    elif '멈춰' in N:
        speak('네 알겠습니다',0)
        playsound.playsound('music/remove.wav')
        return 0,hh,driver
    else:
        speak("명령 리스트에 없습니다",0)
        main.do(2)
        return 1,hh,driver
