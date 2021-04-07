#Harshita Gangaswamy
#add the small txt files to a bigger one and make them upper case

from os import path
import os
import sys

dstPath = '/home/ubuntu/DeepSpeech/data/audiosinc/dst'

if( len(sys.argv) < 2 ):
	sys.exit(os.EX_OK)

dir = sys.argv[1]
f = open("biologydata.txt", "a+")
subDirs = os.listdir(path.join(dstPath, dir))

def copyText(filepath, file):
	with open(path.join(filepath, file)) as tmp:
		for line in tmp:
			f.write(line.upper() + "\n")

for sdir in subDirs:
	if  "." not in sdir:
		filepath = path.join(dstPath, dir, sdir)
		for file in os.listdir(filepath):
			if file.endswith(".txt"):
				copyText(filepath, file)

