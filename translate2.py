#Harshita Gangaswamy

import speech_recognition as sr
from os import path
import re
import inflect
import sys
import os
import time

dstPath = '/home/ubuntu/DeepSpeech/data/audiosinc/dst'

if( len(sys.argv) < 2 ):
	sys.exit(os.EX_OK)

topDir = sys.argv[1]
#subDir = sys.argv[2]
subPath = path.join(dstPath, topDir)
subdir = os.listdir(subPath)

# you can have ' and  in the text
def cleanText(myText):
    temp = re.sub('[^A-Za-z0-9\s]+', '', myText)
    words = temp.split()
    sentence = ""
    p = inflect.engine()
    for w in words:
        t = w
        t1 = re.sub('[^0-9]+', '', w)
        if ( t1 !="" ):
            t = re.sub('-', ' ', p.number_to_words(t1))
            t = re.sub(',', '', t)
        sentence += t+" "
    return sentence.lower()


fx=open(filePath+".lst", "a+")

for d in subdirs:
    if "." not in d:
        files = os.listdir(path.join(subPath, d))
        for AUDIO_FILE in files:
            try:
                r = sr.Recognizer()
                with sr.AudioFile(path.join(filePath, AUDIO_FILE)) as source:
                    audio = r.record(source)
                    text = r.recognize_google(audio)
                    AUDIO_FILE = re.sub('.wav', '.txt', AUDIO_FILE)
                    ft = open(path.join(filePath, AUDIO_FILE), "w")
                    ft.write(cleanText(text))
                    ft.close()
            except:
                fx.write(AUDIO_FILE+"\n")
            time.sleep(5)
fx.close()
