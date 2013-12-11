#!/usr/bin/env python
# -*- coding: utf-8 -*-

from plp import PLP
import fileinput
import re
import sys

p = PLP()

separator = r'#\d+'
separatorPattern = re.compile(separator)

bodziecWord = None

inputLines = []
containingLines = []
    
def main():
    global inputLines
    forms = getForms()
    # print(forms)
    inputLines = readInput()
    parseLines(forms)
    paragraphs = sorted(getParagraphs())
    # print("Found", len(paragraphs), "paragraphs with given word")
    printParagraphs(paragraphs)
    
def printParagraphs(paragraphs):
    for begin, end in paragraphs:
        for i in range(begin, end):
            print(inputLines[i]),
        print("")

def parseLines(forms):
    for i, line in enumerate(inputLines):
        for form in forms:
            if form in line:
                containingLines.append(i)
                break

def getForms():
    return map(lambda x : p.forms(x), p.orec(bodziecWord))[0]

def getParagraphs():
    paragraphs = set()
    for lineNumber in containingLines:
        paragraphs.add(getParagraph(lineNumber))
    return paragraphs

def getParagraph(lineNumber):
    begin = getParagraphBegin(lineNumber)
    end = getParagraphEnd(lineNumber)
    return begin, end

def getParagraphBegin(lineNumber):
    for line in range(lineNumber, 0, -1):
        if(separatorPattern.match(inputLines[line])):
            return line
    return 0

def getParagraphEnd(lineNumber):
    length = len(inputLines)
    for line in range(lineNumber, length):
        if(separatorPattern.match(inputLines[line])):
            return line
    return 0

def readInput():
    inputLines = []
    for line in fileinput.input(sys.argv[2]):
        inputLines.append(line.decode("utf-8"))
    return inputLines

if __name__ == "__main__":
    try:
        if len(sys.argv) < 3:
            sys.exit("Usage: %s <bodziec-word> <parseFile>" % sys.argv[0])
        bodziecWord = sys.argv[1].decode("utf-8")
        main()
    except KeyboardInterrupt:
        print("Oh, man! There's no results yet... See you later!")    
