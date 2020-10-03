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

def name2(data):
    ww = ""
    for i in range(len(data.split())):
        if ('자비스' in data.split()[i]) == False:
            ww = ww + " " + data.split()[i]
    return ww
def do1(hh,driver):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        tts = gTTS(text='혹시 다시 말씀하실거면 "예" 라고 말씀해주세요', lang='ko')
        filename = 'data1.mp3'
        tts.save(filename)
        playsound.playsound(filename)
        os.remove('data1.mp3')
        print("Please say what you have me do")
        audio = r.listen(source)
    try:
        data = r.recognize_google(audio, language='ko')
        ok = check.ok(data)
        if ok == 1:
            data = do(0)
        gg,hh,driver,kk = check.check(data,hh,driver)
    except sr.UnknownValueError:
        playsound.playsound('music/error1.mp3')
    except sr.RequestError as e:
        playsound.playsound('music/error2.mp3')
    except:
        playsound.playsound('music/error1.mp3')
def do(ok):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if ok == 0:
            tts = gTTS(text='시킬 것을 말씀해주세요.', lang='ko')
        if ok == 1:
            tts = gTTS(text='다시 한 번 말씀해주세요.', lang='ko')
        filename = 'data1.mp3'
        tts.save(filename)
        playsound.playsound(filename)
        os.remove('data1.mp3')
        print("Please say what you have me do")
        audio = r.listen(source)
    try:
        data = r.recognize_google(audio, language='ko')
        if data == "" or data == None:
            data = do(1)
        else:
            return data
    except sr.UnknownValueError:
        playsound.playsound('music/error1.mp3')
    except sr.RequestError as e:
        playsound.playsound('music/error2.mp3')

if __name__ == "__main__":   
    gg = 1
    hh = 0
    driver = -1
    translator = Translator()
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("call by '자비스'")
            audio = r.listen(source)
        try:
            data = r.recognize_google(audio, language='ko')
            if '자비스' in data and name2(data) != '':
                print(name2(data))
                playsound.playsound('music/startmusic.wav')
                gg,hh,driver= check.check(name2(data),hh,driver)
                playsound.playsound('music/endmusic.wav')
            elif data == '자비스':
                playsound.playsound('music/startmusic.wav')
                data1 = do(0)
                gg,hh,driver,kk = check.check(data1,hh,driver)
                playsound.playsound('music/endmusic.wav')
            write.make(data)
            if gg == 0:
                break
        except sr.UnknownValueError:
            playsound.playsound('music/error1.mp3')
        except sr.RequestError as e:
            playsound.playsound('music/error2.mp3')
