#Harshita Gangaswamy

from pydub import AudioSegment
from os import path
import re
import sys
import os


dstPath = '/home/ubuntu/DeepSpeech/data/audiosinc/dst'
outputPath = '/opt/projects/1min/'

if( len(sys.argv) < 2 ):
    sys.exit(os.EX_OK)

dir = sys.argv[1]
subdirs = os.listdir(path.join(dstPath, dir))

for sd in subdirs:
    if  "." not in sd:
        files = os.listdir(path.join(dstPath, dir, sd))
        for file in files:
            if file.endswith(".wav"):
                audio = AudioSegment.from_wav(path.join(dstPath, dir, sd, file))
                if(audio.duration_seconds >= 55 and audio.duration_seconds <= 70):
                    TEXT_FILE = re.sub('.wav', '.txt', file)
                    if TEXT_FILE in files:
                        f = open(outputPath + sd + TEXT_FILE, "w")
                        with open(path.join(dstPath, dir, sd, TEXT_FILE)) as tempf:
                            text = tempf.read()
                            f.write(text)
                        f.close()
                        audio.export(outputPath + sd + file, format = "wav")
