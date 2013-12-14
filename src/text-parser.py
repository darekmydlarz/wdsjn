#!/usr/bin/env python
# -*- coding: utf-8 -*-

from plp import PLP
import sys
import os
import codecs
from HTMLParser import HTMLParser
from collections import namedtuple

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()        

InputType = namedtuple('InputType', 'endswith encoding sep')
prus = InputType('.htm', 'iso-8859-2', '\n\n')
nkjp = InputType('text.xml', 'utf-8', '\n\n')
pap = InputType('pap-all.not', 'iso-8859-2', '#')

inputType, forms = None, None

def main(bodziec):
	global forms, inputType
	inputType = getInputType()
	forms = getForms(bodziec)
	traverse()

def getInputType():
	inputType = prus if sys.argv[3] == "prus" else nkjp if sys.argv[3] == "nkjp" else pap if sys.argv[3] == "pap" else None
	if not inputType:
		raise Exception("You choose wrong input type. Allowed are only: prus, nkjp, pap")
	return inputType

def getForms(bodziec):
	return map(lambda x : PLP().forms(x), PLP().orec(bodziec))[0]

def traverse():
	for path, dirs, files in os.walk(sys.argv[2]):
		dirs.sort()
		for f in files:
			if f.lower().endswith(inputType.endswith):
				readFileAndPrintResults(path + os.sep + f)
				
def readFileAndPrintResults(filepath):
	fileParagraphs = readFile(filepath)
	if fileParagraphs:
		print(filepath)
		for p in fileParagraphs:
			print(p + "\n")

def printFile(filepath):
	f = codecs.open(filepath, 'r', inputType.encoding)
	print(strip_tags("".join(f.readlines())))

def readFile(filepath):
	f = codecs.open(filepath, 'r', inputType.encoding)
	paragraphs, p = [], ""
	containsStimulant = False
	for line in f.readlines():
		line = strip_tags(line).strip()
		if not line or inputType.sep in line:
			# end of paragraph
			if containsStimulant:
				paragraphs.append(p.strip())
			containsStimulant = False
			p = ""

		if any(form in line for form in forms):
			containsStimulant = True
		p += line + " "

	# flushing left lines
	if p and containsStimulant:
		paragraphs.append(p.strip())
	return paragraphs

if __name__ == "__main__":
    try:
        if len(sys.argv) < 4:
            sys.exit("Usage: %s <bodziec-word> <dir-with-files> <prus|nkjp|pap>" % sys.argv[0])
    	reload(sys)
    	sys.setdefaultencoding("utf-8")
        main(sys.argv[1].decode("utf-8"))
    except KeyboardInterrupt:
        print("Oh, man! There's no results yet... See you later!")    
    except Exception as e:
    	print(e)
