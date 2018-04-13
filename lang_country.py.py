# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 20:00:14 2017

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
        print(tweet['user']['name'])
        print(tweet['text'])
        tweets_data.append(tweet)
    except:
        continue  


import pandas as pd
import matplotlib.pyplot as plt

tweets = pd.DataFrame()

tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)


tweets_by_lang = tweets['lang'].value_counts()


fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')

tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')


 
 
tweets_by_country = tweets['country'].value_counts()
 
fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Countries', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')



