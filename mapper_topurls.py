# -*- coding: utf-8 -*-
"""
Created on Sat Dec 02 15:28:31 2017

@author: akash
"""

import sys
import re
    
def extract_link(text):
    regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    match = re.search(regex, text)
    if match:
        return match.group()
    return ''




for line in sys.stdin:
    if line: 
        for word in line.strip().split(" "):
		  word = (extract_link(word))		  
		  if len(word) > 1:
		  	print '%s\t%s' %(word, 1)


		
                
                



          
