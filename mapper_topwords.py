#!/usr/bin/python

import sys
import re


stopwords = ['still', 'the', 'rt', 'a', 'and', 'to', '', 'on', 'for', 'of', 'i', 'at', 'you', '-', 'is', 'in', 'de', 'have', 'e', 'eu', 'has']

def extract_link(text):
    regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    match = re.search(regex, text)
    if match:
        return match.group()
    return ''


for line in sys.stdin:
	if line: 
		for word in line.strip().split(" "):
			if not word.startswith('#'):
				word = word.lower()
                                if word not in stopwords:
                                           if word not in (extract_link(word)):
						if len(word) > 4:
							print '%s\t%s' %(word, 1)




