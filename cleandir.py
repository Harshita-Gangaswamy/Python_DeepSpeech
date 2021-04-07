#Harshita Gangaswamy

from pydub import AudioSegment
from os import path
import re
import sys
import os

optPath = '/opt/projects/'

if( len(sys.argv) < 3 ):
    sys.exit(os.EX_OK)

dir = sys.argv[1]
minSec = int(sys.argv[2])
outputPath = optPath + dir

files = os.listdir(outputPath)
fx = open("deletefiles" + dir + ".sh", "w")

for file in files:
    filePath = path.join(outputPath, file)
    if file.endswith(".txt"):
        AUDIO_FILE = re.sub('.txt', '.wav', file)
        if AUDIO_FILE not in files:
            fx.write("rm " + filePath + "\n")
    elif file.endswith(".wav"):
        audio = AudioSegment.from_wav(filePath)
        if audio.duration_seconds < minSec:
            fx.write("rm " + filePath + "\n")
            TEXT_FILE = re.sub('.wav', '.txt', file)
            fx.write("rm " + path.join(outputPath, TEXT_FILE) + "\n")
fx.close()
