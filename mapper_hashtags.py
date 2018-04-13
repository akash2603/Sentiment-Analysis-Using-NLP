#!/usr/bin/python

import sys

for line in sys.stdin:
	if line: 
    		for word in line.strip().split(" "):		
			if word.startswith('#'):
				word = word.replace('#', '').lower()
                        	print '%s\t%s' %(word, 1)
