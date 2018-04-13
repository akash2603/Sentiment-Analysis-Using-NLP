# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 16:06:15 2017

@author: akash
"""

#followers_count


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
        (tweet['user']['verified'])
        (tweet['user']['name']), (tweet['user']['followers_count'])        
        tweets_data.append(tweet)
    except:
        continue
    
    
import pandas as pd

elon_followers = pd.DataFrame()
elon_followers['name'] = map(lambda tweet: tweet['user']['name'], tweets_data)
elon_followers['followers_count'] = map(lambda tweet: tweet['user']['followers_count'], tweets_data)
elon_followers['verified'] = map(lambda tweet: tweet['user']['verified'], tweets_data)

elon_followers = elon_followers.sort_values(['followers_count'], ascending=[False])
print(elon_followers.loc[elon_followers['verified'] == True])
#print(elon_followers)



    

