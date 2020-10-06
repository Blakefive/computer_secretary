import ctypes
user = ctypes.windll.user32

HEX = 0xAD #가상키 코드

user.keybd_event(HEX,0,1,0) #키 내리기
user.keybd_event(HEX,0,2,0) #키 올리기
