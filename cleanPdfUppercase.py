#Harshita Gangaswamy

from num2words import num2words
from os import path
import sys
import os
import re


filePath = '/home/ubuntu/DeepSpeech/data/audiosinc/booktext/'

if( len(sys.argv) < 2 ):
    sys.exit(os.EX_OK)

file = sys.argv[1]
f = open(filePath + file)
lines = f.readlines()
f.close()

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

with open(filePath + file, "w") as f:
    for line in lines:
        elements = line.split()
        for e in elements:
#            print(e)
#            print(type(e))
            if re.search("\d,\d\d\d", e):
                s = e.replace(",", '')
                if s.isnumeric():
                    n = int(s)
                    snum = num2words(n).upper()
                    f.write(snum + " ")
                elif isfloat(s):
                    d = float(s)
                    snum = num2words(d).upper()
                    f.write(snum + " ")
            elif "\"" in e:
                f.write(e.replace("\"", '') + " ")
            elif e != "\"":
                f.write(e + " ")
        f.write("\n")
