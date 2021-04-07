#Harshita Gangaswamy

from nltk.tokenize import TweetTokenizer
from os import path
import PyPDF2
import textract
import sys
import os
import re


bookPath = '/opt/projects/deepspeech/bin/books/'
filePath = '/opt/projects/deepspeech/bin/books/'
characters = ['(', ')', ';', ':', '[', ']', ',', '{', '}', '+', '-', '=', '$', '%', '^', '&', '*', '/', '\\', '<', '>', '\'']
punctuation = ['!', '?', '.']
notwanted = ['x80', 'ao7D', 'x0c']
tknzr = TweetTokenizer()

if( len(sys.argv) < 2 ):
    sys.exit(os.EX_OK)

book = sys.argv[1]
bookPath = bookPath + book

pdfBook = open(bookPath, "rb")
pdfReader = PyPDF2.PdfFileReader(pdfBook)
b = re.sub('.pdf', '.txt', book)
f = open(filePath + b, "w")

num_pages = pdfReader.numPages
count = 0
text = ""

while count < num_pages:
    page = pdfReader.getPage(count)
    text += page.extractText()
    print(count)

    if text == "":
        text = textract.process(bookPath, method='tesseract', language='eng')
        text = str(text)

    splitText = text.split("\\n")
    text = ""
    for item in splitText:
        text += item + " "
#    print(text)
    splitText = text.split("#")
    text = ""
    for item in splitText:
        text += item + " "
    splitText = text.split("@")
    text = ""
    for item in splitText:
        text += item + " "
    splitText = text.split("_")
    text = ""
    for item in splitText:
        text += item + " "
    tokens = tknzr.tokenize(text)
#    print(tokens)
    for t in tokens:
        if t in punctuation:
            f.write("\n")
        elif t == 'xe2':
            f.write("\'")
        elif "x99" in t:
            if len(t) >= 4:
                f.write(t[3].upper())
        elif t not in characters and t not in notwanted and "http" not in t:
            f.write(" " + t.upper())
    count +=1

f.close()
pdfBook.close()
