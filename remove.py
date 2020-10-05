from gtts import gTTS

tts = gTTS(text='에러 났어요', lang='ko')
filename = 'music/error.mp3'
tts.save(filename)
playsound.playsound(filename)
