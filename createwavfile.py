#Harshita Gangaswamy

from os import path
import sys
import os


testpath = '/home/ubuntu/DeepSpeech/data/audiosinc/testwavc'
files = os.listdir(testpath)
f = open("werdata.csv", "w")
f.write("file,google,deepspeech,biology1\n")

for file in sorted(files):
    f.write(file + "\n")
