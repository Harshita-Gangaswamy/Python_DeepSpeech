#Harshita Gangaswamy

from pydub import AudioSegment
from pydub.silence import split_on_silence
from os import path
import sys
import os

srcPath = '/home/ubuntu/DeepSpeech/data/audiosinc/src'
dstPath = '/home/ubuntu/DeepSpeech/data/audiosinc/dst'

if( len(sys.argv) < 2 ):
    sys.exit(os.EX_OK)

dir = sys.argv[1]
files = os.listdir(path.join(srcPath, dir))

def splitFile(dirPath, wavfile):
    wavfile = wavfile.set_frame_rate(16000)
    wavfile = wavfile.set_channels(1)
    chunks = split_on_silence( wavfile, min_silence_len=400, silence_thresh=-45, keep_silence=200 )

    fx=open(dirPath + ".txt", "a+")
    for i, chunk in enumerate(chunks):
        chunk.export(dirPath+"/"+dir+"{:04d}.wav".format(i), format="wav")

for file in files:
    i = 0
    if file.endswith(".wav"):
        dirName = dir + "{:03d}".format(i)
        wavfile = AudioSegment.from_wav(path.join(srcPath, dir, file))
        splitFile(path.join(dstPath, dir), wavfile)
