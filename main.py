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
import youtube
import write
import threading
import sys

def name2(data):
    ww = ""
    for i in range(len(data.split())):
        if ('자비스' in data.split()[i]) == False:
            ww = ww + " " + data.split()[i]
    return ww
def do1(hh,driver):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        tts = gTTS(text='혹시 다시 말씀하실거면 ".응." 라고 말씀해주세요', lang='ko')
        filename = 'data1.mp3'
        tts.save(filename)
        playsound.playsound(filename)
        os.remove('data1.mp3')
        print("If you want to say again, you say '응'")
        audio = r.listen(source)
    try:
        data = r.recognize_google(audio, language='ko')
        ok = check.ok(data)
        if ok == 1:
            data = do(0)
        gg,hh,driver,kk = check.check(data,hh,driver)
        if '멈춰' in data:
            sys.exit("")
    except sr.UnknownValueError:
        playsound.playsound('music/error1.mp3')
    except sr.RequestError as e:
        playsound.playsound('music/error2.mp3')

def do2():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            tts = gTTS(text='다시 한 번 말씀해주세요.', lang='ko')
            write.make('r' + '다시 한 번 말씀해주세요.')
            filename = 'data1.mp3'
            tts.save(filename)
            playsound.playsound(filename)
            os.remove('data1.mp3')
            print("Please say what you have me do again")
            audio = r.listen(source)
        try:
            data = r.recognize_google(audio, language='ko')
            if data != "" and data != None:
                return data
        except sr.UnknownValueError:
            playsound.playsound('music/error1.mp3')
        except sr.RequestError as e:
            playsound.playsound('music/error2.mp3')
        
def do(ok):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if ok == 0:
            tts = gTTS(text='시킬 것을 말씀해주세요.', lang='ko')
            write.make('r' + '시킬 것을 말씀해주세요.')
        filename = 'data1.mp3'
        tts.save(filename)
        playsound.playsound(filename)
        os.remove('data1.mp3')
        print("Please say what you have me do")
        audio = r.listen(source)
    try:
        data = r.recognize_google(audio, language='ko')
        if data == "" or data == None:
            data = do2()
        return data
    except sr.UnknownValueError:
        data = do2()
        return data
    except sr.RequestError as e:
        playsound.playsound('music/error2.mp3')

def cpu_name(ok):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if ok == 0:
            tts = gTTS(text='cpu 이름만 말해주세요.', lang='ko')
            write.make('r' + 'cpu 이름만 말해주세요.')
        filename = 'data1.mp3'
        tts.save(filename)
        playsound.playsound(filename)
        os.remove('data1.mp3')
        print("Please say the cpu which you want to know")
        audio = r.listen(source)
    try:
        data = r.recognize_google(audio, language='ko')
        if data == "" or data == None:
            data = do2()
        write.make('m' + data)
        return data
    except sr.UnknownValueError:
        data = do2()
        write.make('m' + data)
        return data
    except sr.RequestError as e:
        playsound.playsound('music/error2.mp3')

def talk_en(ok):
    translator = Translator()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if ok == 0:
            tts = gTTS(text='번역할 내용을 영어로 알려주세요', lang='ko')
            write.make('r' + '번역할 내용을 영어로알려주세요')
        filename = 'data1.mp3'
        tts.save(filename)
        playsound.playsound(filename)
        os.remove('data1.mp3')
        print("Please say what you want to translate into Korean")
        audio = r.listen(source)
    try:
        data = r.recognize_google(audio, language='en')
        if data == "" or data == None:
            data = do2()
        write.make('m' + data)
        data = translator.translate(data, dest="ko").text
        return data
    except sr.UnknownValueError:
        data = do2()
        data = translator.translate(data, dest="ko").text
        write.make('m' + data)
        return data
    except sr.RequestError as e:
        playsound.playsound('music/error2.mp3')

def talk_ko(ok):
    translator = Translator()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if ok == 0:
            tts = gTTS(text='번역할 내용을 한국어로 알려주세요', lang='ko')
            write.make('r' + '번역할 내용을 한국어로 알려주세요')
        filename = 'data1.mp3'
        tts.save(filename)
        playsound.playsound(filename)
        os.remove('data1.mp3')
        print("Please say what you want to translate into English")
        audio = r.listen(source)
    try:
        data = r.recognize_google(audio, language='ko')
        if data == "" or data == None:
            data = do2()
        write.make('m' + data)
        data = translator.translate(data, dest="en").text
        return data
    except sr.UnknownValueError:
        data = do2()
        data = translator.translate(data, dest="en").text
        write.make('m' + data)
        return data
    except sr.RequestError as e:
        playsound.playsound('music/error2.mp3')

def day_split(text):
    day = text.split()
    return day[0][:-1] + "-" + day[1][:-1] + day[2][:-1]
        
def mbirthday(ok):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if ok == 0:
            tts = gTTS(text='생일 날짜만 말해주세요.', lang='ko')
            write.make('r' + '생일 날짜만 말해주세요.')
        filename = 'data1.mp3'
        tts.save(filename)
        playsound.playsound(filename)
        os.remove('data1.mp3')
        print("Please say your birthday")
        audio = r.listen(source)
    try:
        data = r.recognize_google(audio, language='ko')
        if data == "" or data == None:
            data = do2()
        write.make('m' + data)
        return day_split(data)
    except sr.UnknownValueError:
        data = do2()
        write.make('m' + data)
        return day_split(data)
    except sr.RequestError as e:
        playsound.playsound('music/error2.mp3')

if __name__ == "__main__":
    f = open('data/mbirthday.txt','r')
    line = f.readline()
    f.close()
    birthday_year = '2020'
    birthday = '930'
    if line != '':
        mbirthday_year,mbirthday = int(line.split('-')[0]),int(line.split('-')[1])
    elif line == '':
        line = mbirthday(0)
        mbirthday_year,mbirthday = int(line.split('-')[0]),int(line.split('-')[1])
        f = open('data/mbirthday.txt','w')
        line = f.write(line)
        f.close()
    gg = 1
    hh = 0
    driver = -1
    translator = Translator()
    tm = time.localtime()
    if birthday == str(tm.tm_mon)+str(tm.tm_mday):
        check.speak('제가 벌써 ' + str((int(str(tm.tm_year)) - int(birthday_year))+1) +'살 입니다. 만들어 주셔서 감사합니다.',0)
    if mbirthday == str(tm.tm_mon)+str(tm.tm_mday):
        check.speak('생일 축하합니다 ' + str((int(str(tm.tm_year)) - int(mbirthday_year))+1) +'살이시네요.',0)
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("call by '자비스'")
            audio = r.listen(source)
        try:
            data = r.recognize_google(audio, language='ko')
            print(data)
            if '자비스' in data and name2(data) != '':
                print(name2(data))
                playsound.playsound('music/startmusic.wav')
                gg,hh,driver,kk= check.check(name2(data),hh,driver)
                playsound.playsound('music/endmusic.wav')
            elif data == '자비스':
                playsound.playsound('music/startmusic.wav')
                data1 = do(0)
                gg,hh,driver,kk = check.check(data1,hh,driver)
                print(data1)
                playsound.playsound('music/endmusic.wav')
                write.make('m' + data1)
            write.make('m' + data)
            if gg == 0:
                break
            t = threading.Thread(target=youtube.loop_skip, args=(driver, ))
            t.start()
            try:
                if '멈춰' in name2(data):
                    sys.exit("")
            except NameError:
                try:
                    if '멈춰' in data1:
                        sys.exit("")
                except NameError:
                    pass
        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            playsound.playsound('music/error2.mp3')
        except OSError:
            pass
