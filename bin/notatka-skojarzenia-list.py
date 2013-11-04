#!/usr/bin/env python27
# -*- coding: utf-8 -*-
import os

from plp import PLP
import sys
import fileinput
import re
from collections import OrderedDict

wordPattern = r'\b[^\W\d]+\b'
wordObj = re.compile(wordPattern, re.IGNORECASE | re.UNICODE)

bodziecNotatkiFile = None
bodziecWord = None

skojarzeniaDict = OrderedDict()
p = PLP()

def main():
    buildSkojarzeniaDict()
    processInput()

def buildSkojarzeniaDict():
    global skojarzeniaDict
    for i in xrange(3, len(sys.argv)):
        skojarzenieFile = extractFileName(i)
        skojarzeniaDict[skojarzenieFile] = OrderedDict()
        for line in fileinput.input(sys.argv[i], openhook=fileinput.hook_encoded("utf8")):
            word, cardinality = extractCsvRow(line)
            if word.strip() and p.orec(word):
                skojarzeniaDict[skojarzenieFile][word] = int(cardinality)

def extractFileName(index):
    fileName = os.path.basename(sys.argv[index]).split(".")[0]
    return decorateFileName(fileName, index)

def decorateFileName(fileName, index):
    fileName = " ".join(["#", fileName])
    return '#' + fileName if index > 3 else fileName

def extractCsvRow(line):
    return tuple(line.strip().replace("\"", "").split(","))

def processInput():
    # note is a set of words (in their basic form) which given note was build of
    note = set()
    for line in fileinput.input(bodziecNotatkiFile, openhook=fileinput.hook_encoded("utf8")):
        print line,
        if line.strip():
            note.update(processNoteLine(line))
            continue
        processNote(note)
        note.clear()

# @return set of words in their basic form for given line
def processNoteLine(line):
    processed = set()
    for word in wordObj.findall(line):
        if word.strip() and p.orec(word):
            for index in p.orec(word):
                processed.add(p.bform(index))
    return processed

def processNote(note):
    for key, values in skojarzeniaDict.iteritems():
        print(key)
        for value in values:
            if value in note:
                items = ['%s', '%s']
                if value == bodziecWord:
                    items.append('%%')
                print(','.join(items) % (value, values[value]))
    print("")

if __name__ == "__main__":
    try:
        if len(sys.argv) < 4:
            sys.exit("Usage: %s <bodziec-word> <bodziec-notatki-file> <skojarzenie-file> ..." % sys.argv[0])
        bodziecWord = sys.argv[1].decode("utf-8")
        bodziecNotatkiFile = sys.argv[2]
        main()
    except KeyboardInterrupt:
        print("Oh, man! There's no results yet... See you later!")