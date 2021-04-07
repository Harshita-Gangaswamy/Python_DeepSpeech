#Harshita Gangaswamy

import speech_recognition as sr
from pydub import AudioSegment
from os import path
import re
import sys
import os
import time


dstPath = '/home/ubuntu/DeepSpeech/data/audiosinc/dst'
outputPath = '/opt/projects/1min/'
silence = '/opt/projects/noise/silent.wav'

if( len(sys.argv) < 2 ):
	sys.exit(os.EX_OK)

topDir = sys.argv[1]
filePath = path.join(dstPath, topDir)
subdirs = os.listdir(filePath)
timesec = 0
part = 1

fx=open(outputPath + topDir +".lst", "a+")

def makeFile(piece, sd, file):
    piece = piece.set_frame_rate(16000)
    piece = piece.set_channels(1)
    try:
        r = sr.Recognizer()
        with sr.AudioFile(piece) as source:
            a = r.record(source)
            text = r.recognize_google(a)
            return text
    except:
        fx.write(sd + file + "\n")

for sd in subdirs:
    if "." not in sd:
        files = sorted(os.listdir(path.join(dstPath, topDir, sd)))
        part = 1
        time = 0
        f = open(outputPath + sd + "pt" + str(part) + ".txt", "w")
        newaudio = AudioSegment.from_wav(silence)
        for file in files:
            if file.endswith(".txt") and timesec <= 50:
                AUDIO_FILE = re.sub('.txt', '.wav', file)
                audio = AudioSegment.from_wav(path.join(dstPath, topDir, sd, AUDIO_FILE))
                if (timesec + audio.duration_seconds) >= 70:
                    secNeed = 60 - timesec
                    firstpart = audio[0:secNeed]
                    newaudio = newaudio + firstpart
                    text = makeFile(firstpart, sd, file)
                    if text:
                        f.write(text)
                    f.close()
                    newaudio.export(outputPath + sd + "pt" + str(part) + ".wav", format = "wav")
                    part = part + 1
                    f = open(outputPath + sd + "pt" + str(part) + ".txt", "w")
                    lastpart = audio[secNeed:audio.duration_seconds]
                    text = makeFile(lastpart, sd, file)
                    if text:
                        f.write(text)
                    t = audio.duration_seconds - secNeed
                else:
                    tempf = open(path.join(filePath, sd, file))
                    text = tempf.read()
                    tempf.close()
                    f.write(text)
                    newaudio = newaudio + audio
                    timesec = timesec + audio.duration_seconds
            elif file.endswith(".txt") and timesec > 50:
                f.close()
                newaudio.export(outputPath + sd + "pt" + str(part) + ".wav", format = "wav")
                part = part + 1
                f = open(outputPath + sd + "pt" + str(part) + ".txt", "w")
                tempf = open(path.join(filePath, sd, file))
                text = tempf.read()
                tempf.close()
                f.write(text)
                newaudio = newaudio + audio
                timesec = audio.duration_seconds
        f.close()
        newaudio.export(outputPath + sd + "pt" + str(part) + ".wav", format = "wav")

fx.close()
