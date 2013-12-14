#!/usr/bin/env python
# -*- coding: utf-8 -*-

from plp import PLP
import sys
import os
import codecs
from HTMLParser import HTMLParser

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

def main(bodziec):
	traverse()

def getForms(bodziec):
	return map(lambda x : p.forms(x), p.orec(bodziec))[0]

def traverse():
	for path, dirs, files in os.walk(sys.argv[2]):
		for f in files:
			if f.lower().endswith("htm"):
				readFile(path + os.sep + f)

def readFile(filepath):
	f = codecs.open(filepath, 'r', 'iso-8859-2')
	lines = strip_tags("".join(f.readlines()))
	print(lines)


if __name__ == "__main__":
    try:
        if len(sys.argv) < 3:
            sys.exit("Usage: %s <bodziec-word> <prus-dir>" % sys.argv[0])
    	reload(sys)
    	sys.setdefaultencoding("utf-8")
        main(sys.argv[1].decode("utf-8"))
    except KeyboardInterrupt:
        print("Oh, man! There's no results yet... See you later!")    