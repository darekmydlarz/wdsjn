#!/usr/bin/env python3

import fileinput
import re
import sys

separator = r'#\d+'
separatorPattern = re.compile(separator)

bodziecPattern = None

inputLines = []
containingLines = []
    
def main():
    global inputLines
    inputLines = readInput()
    parseLines()
    paragraphs = sorted(getParagraphs())
    # print("Found", len(paragraphs), "paragraphs with given word")
    printParagraphs(paragraphs)
    
def printParagraphs(paragraphs):
    for begin, end in paragraphs:
        print("".join(map(str, inputLines[begin:end])))

def parseLines():
    for i, line in enumerate(inputLines):
        if(bodziecPattern.match(line)):
            containingLines.append(i)
    

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
        inputLines.append(line)
    return inputLines

if __name__ == "__main__":
    try:
        if len(sys.argv) < 3:
            sys.exit("Usage: %s <bodziec-word> <parseFile>" % sys.argv[0])
        bodziecWord = r'.*'+sys.argv[1]+r'.*'
        bodziecPattern = re.compile(bodziecWord, re.I)
        main()
    except KeyboardInterrupt:
        print("Oh, man! There's no results yet... See you later!")    
