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
import check
import threading

title_slst = [] # stringList
option_wd = webdriver.ChromeOptions() # option in webdriver
option_wd.add_argument('headless')
option_wd.add_argument('window-size=1920x1080')
option_wd.add_argument("disable-gpu")

def loop_skip(driver):
    while True:
        try:
            driver.find_element_by_xpath('//*[@id="skip-button:6"]/span/button').click()
        except:
            pass

def tellcheck(data):
    if '첫' in data or '일' in data or '1' in data :
        return 1
    elif '두' in data or '이' in data or '2' in data :
        return 2
    elif '세' in data or '삼' in data or '3' in data :
        return 3
    elif '네' in data or '사' in data or '4' in data :
        return 4
    elif '다섯' in data or '오' in data or '5' in data :
        return 5
    else:
        tts = gTTS(text="다시 한번 말해주세요", lang='ko')
        filename = 'data.mp3'
        tts.save(filename)
        playsound.playsound(filename)
        os.remove('data.mp3')

def tell():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tell me what to tell me")
        audio = r.listen(source)

    try:
        data = r.recognize_google(audio, language='ko')
        print("Google Speech Recognition thinks you said : "
              + data)
        return tellcheck(data)
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        pass
    except Traceback:
        pass

    
def sort(text):
    number = {1:' 첫 번째. ',2:' 두 번째. ',3:' 세 번째. ',4:' 네 번째. ',5:' 다섯 번째. '}
    M = " 제목을 말씁해드리겠습니다.  "
    for i in range(len(text)):
        M = M +number[i+1]+ text[i][2:] + "."
    return M +"  .......중 하나를 순서로 말해주세요   "

def getTitles(findName,driver,pp):
    if pp == 0:
        driver.get("https://www.youtube.com/results?search_query=" + findName)
        driver.implicitly_wait(3)
        title_slst = [str(count+1) + ". "+ value.text for count, value in enumerate(driver.find_elements_by_xpath('//*[@id="video-title"]/yt-formatted-string'))]
        Nlist = title_slst[:5]
        check.speak(sort(Nlist),7)
        data = tell()
        driver.find_elements_by_xpath('//*[@id="video-title"]/yt-formatted-string')[data - 1].click()
    elif pp == 1:
        driver.get("https://www.youtube.com/results?search_query=" + findName)
        driver.implicitly_wait(3)
        check.speak(findName + " 을 유튜브에 찾습니다",3)
    elif pp == 2:
        driver.get("https://www.youtube.com/results?search_query=" + str(findName))
        driver.implicitly_wait(3)
        check.speak('유튜브에서 ' + findName + ' 의 첫 번째의 영상을 실행시킵니다',3)
        driver.find_elements_by_xpath('//*[@id="video-title"]/yt-formatted-string')[0].click()
        

