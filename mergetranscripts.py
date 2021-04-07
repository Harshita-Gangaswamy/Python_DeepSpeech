#Harshita Gangaswamy

from os import path
import sys
import os


dstPath = '/home/ubuntu/DeepSpeech/data/audiosinc/dst'

if( len(sys.argv) < 2 ):
	sys.exit(os.EX_OK)

dir = sys.argv[1]
files = os.listdir(path.join(dstPath, dir))

fx = open(dir + ".txt", "w")

for file in sorted(files):
	if file.endswith(".txt"):
		filePath = path.join(dstPath, dir, file)
		with open(filePath) as tempf:
			text = tempf.read()
			fx.write(text)
