#Harshita Gangaswamy

from jiwer import wer
from os import path
import sys
import os

filepath = '/opt/projects/deepspeech'
corfilepath = '/opt/projects/deepspeech/corrected'

if( len(sys.argv) < 2 ):
        sys.exit(os.EX_OK)

dir = sys.argv[1]

f = open("werdata.csv")
flines = f.readlines()
f.close()
f = open("werdata.csv", "w")

for line in flines:
    if "file" not in line:
        index = flines.index(line)
        line = line.strip()
        parts = line.split(",")
        filename = parts[0]

        cfile = open(path.join(corfilepath, filename))
        text1 = cfile.read()

        tfile = open(path.join(filepath, dir, filename))
        text2 = tfile.read()

        error = round(wer(text1, text2) * 100, 2)
        line = line + "," + str(error) + "\n"
        flines[index] = line

f.writelines(flines)
f.close()
