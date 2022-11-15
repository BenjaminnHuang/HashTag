
import tweepy
import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


consumer_key = 'm389H6eHutIecF7SZjEu1zcjR'
consumer_secret = 'sNTQZl18KGowmHDHFJqPgJoq8M3SVtGe8RY1UY6ztr9yl8lNAs'
access_token = '1584651535933267968-Iq8u3WDEFTGV4IVzoETufQGDGPnwh0'
access_token_secret = 'wHqPJ0eLir3OjopC2MPey7S6cKOLux2Z4TYMfZCdu9K6z'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

userID = 'elonmusk'
keywords = 'Twitter from:elonmusk filter:images'

tweets = tweepy.Cursor(api.search_tweets, q=keywords, lang='en',
        count=5, tweet_mode='extended').items(5)

all_tweets = []

for tw in tweets:
    all_tweets.append(tw)

outtweets = []

idx = 0

for tweet in all_tweets:

    status = api.get_status(tweet.id, include_ext_alt_text=True, tweet_mode='extended')
    hasAlt = 'no'
    alt = 'None'
    if hasattr(status, 'extended_entities'):
        alt = status.extended_entities['media'][0]['ext_alt_text']
        if(alt == None or ''):
            hasAlt = 'no'
        else:
            hasAlt = 'yes'

    temp = []
    
    temp.append(tweet.id_str)
    temp.append(tweet.created_at)
    temp.append(tweet.favorite_count)
    temp.append(tweet.retweet_count)
    temp.append(hasAlt)
    temp.append(alt)
    temp.append(tweet.full_text.encode("utf-8").decode("utf-8"))

    outtweets.append(temp)
        
    idx += 1

df = pd.DataFrame(outtweets,columns=["id","created_at","favorite_count", "retweet_count", 'has alt_text?', 'alt_text', "text"])
df.to_csv('tweets/test_tweets.csv',index=False)
df.head(3)

