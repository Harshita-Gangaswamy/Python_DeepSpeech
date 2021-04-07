#Harshita Gangaswamy

from os import path
import os


filePath = '/opt/projects/deepspeech/corrected'
f = open("werdata.csv", "w")
f.write("file,biology1-1,biology1-2,biology2,biology3,biology5\n")
files = os.listdir(filePath)
for file in sorted(files):
    f.write(file + "\n")
