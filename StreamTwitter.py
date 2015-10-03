# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 23:01:14 2015

@author: 570360
"""
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import sys
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
#TODO .... checkout use of Git   and more

#TODO here is a second change
#TODO here is a third change
#Setting up Twitter API

#consumer key, consumer secret, access token, access secret.
ckey="g3OXvR30RrnytpKjf6W9ubSiz"
csecret="9gnSmeHiTs9zdZQzNIu0jk2iuvQN30icvxadTS8zvRT2RL2uLF"
atoken="2255299502-cN6ZjaMobhzMklnRSNe1iEWGtRzWSKNnwnbiBJM"
asecret="DO5kMhzs2Du16MPUrHeNhl1Nb05xOgS69A8Cr1lbOAS90"
auth=OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
api = tweepy.API(auth)

class listener(StreamListener):

    def on_data(self, data):
        print(data)
        return(True)

    def on_error(self, status):
        print status

#twitterStream = Stream(auth, listener())
#twitterStream.filter(track=["Exxon"])

#Send out a tweet
#api.update_status('This is a tweet about thermal imaging')
#print "User id: " + user.id_str
#
#for status in tweepy.Cursor(api.home_timeline).items(2):
#    # Process a single status
#    print(status.text)

#argfile = str(sys.argv[1])  #This requires a file name in the command line
#filename=open(argfile,'r')
#f=filename.readlines()
#filename.close()
#for line in f:
#    api.update_status(status=line)
#    time.sleep(900)#Tweet every 15 minutes


""" 
for items in tweepy.Cursor(api.search, q="cars", since="2014-10-01", until="2014-10-31").items(5):
    print items.text
    """
def process_status(sta):
    print sta.text
def process_friend(fr):
    print fr.screen_name
    
for follower in tweepy.Cursor(api.followers).items(5):
    print follower.id,follower.screen_name    
# Iterate through all of the authenticated user's friends
for friend in tweepy.Cursor(api.friends).items(5):
    # Process the friend here
    process_friend(friend)
#print api.me()
#print api.retweets_of_me(5)
#print api.trends_available()
for message in tweepy.Cursor(api.home_timeline).items(5):
    print message.text
    print
# Note:  the following has not been updated in Tweepy documentation
# as of 8/21/2015
api.update_status(status="@thermologyguy-find the highest performance thermal infrared camera for equine and medical purposes.  It is all about having no drift.") # Settings must be updated to R/W/Update
## Iterate through the first 200 statuses in the friends timeline
#for status in tweepy.Cursor(api.friends).items(5):
#    # Process the status here
#    process_status(status)   
#    
#    
retrievals=0
while retrievals<5:
    for tweet in tweepy.Cursor(api.search,
                               q="Exxon",
                               rpp=3,
                               result_type="recent",
                               include_entities=True,
                               lang="en").items(4):
        print tweet.created_at, tweet.text
        print
        
        time.sleep(4)     # Tweet every 4 seconds 
        retrievals+=1
