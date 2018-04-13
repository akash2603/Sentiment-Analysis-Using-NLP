# -*- coding: utf-8 -*-
"""
Created on Sun Dec 03 20:38:43 2017

@author: akash
"""

import sys
import json

#set the path to the output file
tweets_data_path = 'D:/Third Semester/Statistics Software/Hadoop/Project/MTA/mta_3rdMarch2018.txt'


#initialize an array and open the output file for reading

tweets_file = open(tweets_data_path, "r")
tweets_data = []
#process each line in output file
for line in tweets_file:
    
    try:
        tweet = json.loads(line)
#        print (tweet['user']['name'])
        tweet['text']
        tweet_text = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet['text'].split()
        
#        tweets_data.append(tweet)
    except:
        continue
        
#print how many tweets were processed
#print len(tweets_data)