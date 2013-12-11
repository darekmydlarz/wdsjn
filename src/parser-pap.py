#!/usr/bin/env python
# -*- coding: utf-8 -*-

from plp import PLP
import sys
import fileinput

p = PLP()
lineSeparator = '#'

def main(bodziec):
	forms = getForms(bodziec)
	paragraphs = getParagraphs(forms)
	printParagraphs(paragraphs)

def getForms(bodziec):
	return map(lambda x : p.forms(x), p.orec(bodziec))[0]

def getParagraphs(forms):
	paragraphs, p = [], []
	containsStimulant = False
	for line in fileinput.input(sys.argv[2]):
		line = line.strip().decode("utf-8")
		# end of paragraph
		if not line or lineSeparator in line:
			if containsStimulant:
				paragraphs.append(p)
			containsStimulant = False
			p = []

		if any(form in line for form in forms):
			containsStimulant = True
		p.append(line)

	# flushing left lines
	if p and containsStimulant:
		paragraphs.append(p)
	return paragraphs

def hasForm(forms, line):
	for form in forms:
		if form in line: return True
	return False

def printParagraphs(paragraphs):
	# print(len(paragraphs))
	for p in paragraphs:
		for line in p: 
			print(line)
		print("")

if __name__ == "__main__":
    try:
        if len(sys.argv) < 3:
            sys.exit("Usage: %s <bodziec-word> <file-to-parse>" % sys.argv[0])
    	reload(sys)
    	sys.setdefaultencoding("utf-8")
        main(sys.argv[1].decode("utf-8"))
    except KeyboardInterrupt:
        print("Oh, man! There's no results yet... See you later!")    