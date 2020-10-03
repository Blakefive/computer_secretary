import time
import os

def make(text):
    if text != "" and text != " ":
        tm = time.localtime()
        name = str(tm.tm_year) + "." + str(tm.tm_mon) + "." + str(tm.tm_mday)
        if os.path.isfile("data/" +name+".txt"):
            f = open("data/" +name+".txt", 'a')
            text = "\n" + text
            f.write(text)
        else:
            f = open("data/" +name+".txt", 'w')
            f.write(text)
        f.close()
