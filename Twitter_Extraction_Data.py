**# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 10:46:16 2017

@author: akash
"""

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "2856476408-8GPKPYhbBgosKA7PiYzo4VbATIeK0HjhuKLF7Ga"
access_token_secret = "r90mBnkaHTTFQxoAwHHcD57mGzOoYlBpq8D6xcL9HJytQ"
consumer_key = "u51rfRFNL3eHXzeNoDw1GShUz"
consumer_secret = "6cOJ1Ni9Mfd2z2BB76Lzjgyw96iNod6VXlvVniTnoajWjopMO5"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by keywords
    stream.filter(track=['MTA','NYCTSubway','NYCTBus','NYCTSubway','LIRR','MetroNorth'])