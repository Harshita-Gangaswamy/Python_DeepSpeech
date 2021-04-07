#Harshita Gangaswamy
#clean up the files more so take out unnecessary spaces and random words

from num2words import num2words
from os import path
import sys
import os
import re


filePath = '/home/ubuntu/DeepSpeech/data/audiosinc/booktext/'
notwanted = ['X9C', 'X9D', 'X0C', 'XC2', 'XAE', 'X98', 'X94','|', 'NAN']

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

#rewrite numbers to words
with open(filePath + file, "w") as f:
    for line in lines:
        if line.strip():
            elements = line.split()
            for e in elements:
                if "-" in e:
                    pos = e.find("-")
                    if e[:pos].isnumeric() and e[pos + 1:].isnumeric():
                        n = int(e[:pos])
                        n2 = int(e[pos + 1:])
                        s = num2words(n).upper()
                        s2 = num2words(n2).upper()
                        s = s.replace(", ", " ")
                        s = s.replace("-", " ")
                        s2 = s2.replace(", ", " ")
                        s2 = s2.replace("-", " ")
                        f.write(s + " TO " + s2 + " ")
                    elif isfloat(e[:pos]) and isfloat(e[pos + 1:]):
                        d = float(e[:pos])
                        d2 = float(e[pos + 1:])
                        s = num2words(d).upper()
                        s2 = num2words(d2).upper()
                        s = s.replace(", ", " ")
                        s = s.replace("-", " ")
                        s2 = s2.replace(", ", " ")
                        s2 = s2.replace("-", " ")
                        f.write(s + " TO " + s2 + " ")
                    else:
                        f.write(e.replace("-", " ") + " ")
                elif ":" in e:
                    pos = e.find(":")
                    if e[:pos].isnumeric() and e[pos + 1:].isnumeric():
                        n = int(e[:pos])
                        n2 = int(e[pos + 1:])
                        s = num2words(n).upper()
                        s2 = num2words(n2).upper()
                        s = s.replace(", ", " ")
                        s = s.replace("-", " ")
                        s2 = s2.replace(", ", " ")
                        s2 = s2.replace("-", " ")
                        f.write(s + " TO " + s2 + " ")
                    elif isfloat(e[:pos]) and isfloat(e[pos + 1:]):
                        d = float(e[:pos])
                        d2 = float(e[pos + 1:])
                        s = num2words(d).upper()
                        s2 = num2words(d2).upper()
                        s = s.replace(", ", " ")
                        s = s.replace("-", " ")
                        s2 = s2.replace(", ", " ")
                        s2 = s2.replace("-", " ")
                        f.write(s + " TO " + s2 + " ")
                    else:
                        f.write(e.replace(":", " ") + " ")
                elif "B'" in e:
                    f.write(e[2:] + " ")
                elif e == "INF" or e == "INFINITY":
                    f.write("INFINITY ")
                elif e.isnumeric():
                    n = int(e)
                    s = num2words(n).upper()
                    s = s.replace(", ", " ")
                    s = s.replace("-", " ")
                    f.write(s + " ")
                elif isfloat(e) and e != "NAN":
                    d = float(e)
#                    print(e)
                    s = num2words(d).upper()
                    s = s.replace(", ", " ")
                    s = s.replace("-", " ")
                    f.write(s + " ")
                elif e not in notwanted and e != "\'" and e != ".":
                    if e[-1] == '\'':
                        e = e[:-1]
                    for nw in notwanted:
                        if nw in e:
                            e = e[3:]
#                print(e)
#                print(elements)
                    f.write(e + " ")
            f.write("\n")
