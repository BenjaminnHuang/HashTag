
import tweepy
import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

# url = "https://cadem.org/state-senate/"
# req = Request(url, headers={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
#                             "Accept-Encoding": "gzip, deflate, br",
#                             "Referer": "https://www.google.com",
#                             'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'})
# webpage = urlopen(req).read()
# soup = BeautifulSoup(webpage, 'html.parser')

# print(soup.text)
# myDivs = soup.find_all("div", {"class" : "apollo-candidate-socialicon apollo-candidate-socialtwitter"})

# link = []

# #getting all the twitter account links of the candidates
# for links in myDivs:
#     for all_link in links.find_all('a', href=True):
#         link.append(all_link['href'])

# twID = []

# #getting twitter id
# for usr in link:
#     result = usr.split('/')[3]
#     result = result.split('?')
#     twID.append(result[0])

# twID.remove('davecortese2020')
# twID.remove('@roth4senate')


consumer_key = 'm389H6eHutIecF7SZjEu1zcjR'
consumer_secret = 'sNTQZl18KGowmHDHFJqPgJoq8M3SVtGe8RY1UY6ztr9yl8lNAs'
access_token = '1584651535933267968-Iq8u3WDEFTGV4IVzoETufQGDGPnwh0'
access_token_secret = 'wHqPJ0eLir3OjopC2MPey7S6cKOLux2Z4TYMfZCdu9K6z'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

userID = 'elonmusk'
keywords = '#BLM filter:images'

tweets = tweepy.Cursor(api.search_tweets, q=keywords, lang='en',
        count=50, tweet_mode='extended').items()

all_tweets = []

for tw in tweets:    
    all_tweets.append(tw)
    
outtweets = [[None] * 6] * len(all_tweets)

for tweet in all_tweets:
    status = api.get_status(tweet.id, include_ext_alt_text=True, tweet_mode='extended')
    hasAlt = 'no'
    if hasattr(status, 'extended_entities'):

        alt = status.extended_entities['media'][0]['ext_alt_text']
        outtweets[5].append(alt)
        hasAlt = 'yes'
    else:
        hasAlt = 'no'

    outtweets[0].append(tweet.id_str)
    outtweets[1].append(tweet.created_at)
    outtweets[2].append(tweet.favorite_count)
    outtweets[3].append(tweet.retweet_count)
    outtweets[4].append(hasAlt)
    outtweets[6].append(tweet.full_text.encode("utf-8").decode("utf-8"))
    
df = pd.DataFrame(outtweets,columns=["id","created_at","favorite_count", "retweet_count", 'has alt_text?', 'alt_text', "text"])
df.to_csv('tweets/test_tweets.csv',index=False)
df.head(3)

