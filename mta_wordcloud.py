# -*- coding: utf-8 -*-
"""
Created on Thu Dec 07 01:39:18 2017

@author: akash
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Dec 06 00:16:52 2017

@author: akash
"""

import sys
import json
from wordcloud import WordCloud, STOPWORDS
from stop_words import get_stop_words
import matplotlib.pyplot as plt


stop_words = get_stop_words('en')
stopwords = set(STOPWORDS)
stopwords.add("https")
stopwords.add("CO")
stopwords.add("RT")


#set the path to the output file
tweets_data_path = 'D:/Third Semester/Statistics Software/Hadoop/Project/MTA/mta_3rdMarch2018.txt'


#initialize an array and open the output file for reading

tweets_file = open(tweets_data_path, "r")
tweets_data = []
word_string = ''
#process each line in output file
for line in tweets_file:
    
    try:
        tweet = json.loads(line)
        #print (tweet['user']['name'])
        tweet_text = tweet['text']
        data = tweet_text.split()
        for word in data:
            if len(word) > 4:
                if word not in stop_words:
                    print ("{0}\t{1}".format(word.lower(),1))
                    word_string += word
                
        tweets_data.append(tweet)
    except:
        continue
    
    
    print(len(tweets_data))
    
wordcloud = WordCloud(max_words=100, background_color = 'white', width = 1200, height = 1000, stopwords=stopwords).generate(word_string)
plt.figure( figsize=(20,10) )
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
        
