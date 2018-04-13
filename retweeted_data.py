# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 17:23:31 2017

@author: akash
"""

import sys
import json

#set the path to the output file
tweets_data_path = 'D:/Third Semester/Statistics Software/Hadoop/Project/MTA/mta_3rdMarch2018.txt'


#initialize an array and open the output file for reading
tweets_data = []
tweets_file = open(tweets_data_path, "r")

#process each line in output file
for line in tweets_file:
    try:
        tweet = json.loads(line)
#        print (tweet['retweeted_status']['text'])
#        print(tweet['user']['notifications'])
        (tweet['text'])
        (tweet['retweeted_status']['retweet_count'])
        (tweet['user']['verified'])
        tweets_data.append(tweet)
    except:
        continue
    
    
import pandas as pd

tweets = pd.DataFrame()

tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
tweets['retweet_count'] = map(lambda tweet: tweet['retweeted_status']['retweet_count'], tweets_data)
tweets['verified'] = map(lambda tweet: tweet['user']['verified'], tweets_data)


tweets = tweets.sort_values(['retweet_count'], ascending=[False])

tweets = tweets.drop_duplicates('text')
print(tweets.loc[tweets['verified'] == True])

        




 
