#Harshita Gangaswamy

from pydub import AudioSegment
from os import path
import sys
import os


dstPath = '/home/ubuntu/DeepSpeech/data/audiosinc/dst'

if( len(sys.argv) < 2 ):
    sys.exit(os.EX_OK)

dir = sys.argv[1]
subdirs = os.listdir(path.join(dstPath, dir))

for sd in subdirs:
    if  "." not in sd:
        print(sd)
        files = os.listdir(path.join(dstPath, dir, sd))
        for file in files:
            if file.endswith(".wav"):
                audio = AudioSegment.from_wav(path.join(dstPath, dir, sd, file))
                if(audio.duration_seconds >= 60):
                    print(file + ", " + str(audio.duration_seconds))
