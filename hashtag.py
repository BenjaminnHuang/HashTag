
import tweepy
import pandas as pd
import requests
from bs4 import BeautifulSoup

# page = requests.get("https://cadem.org/state-senate/")
# soup = BeautifulSoup(page.content, 'html.parser')

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


consumer_key = 'Wc46qw5CVy9JQ2DOzgIlYkKlG'
consumer_secret = 'sNTQZl18KGowmHDHFJqPgJoq8M3SVtGe8RY1UY6ztr9yl8lNAs'
access_token = '1584651535933267968-Iq8u3WDEFTGV4IVzoETufQGDGPnwh0'
access_token_secret = 'wHqPJ0eLir3OjopC2MPey7S6cKOLux2Z4TYMfZCdu9K6z'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

userID = 'elonmusk'
keywords = '2022'

tweets = tweepy.Cursor(api.search_tweets, q=keywords, lang='en',
        count=200, tweet_mode='extended').items(300)

all_tweets = []

for tw in tweets:
    all_tweets.append(tw)

outtweets = [[tweet.id_str, 
            tweet.created_at, 
            tweet.favorite_count, 
            tweet.retweet_count, 
            tweet.full_text.encode("utf-8").decode("utf-8")] 
            for idx,tweet in enumerate(all_tweets)]
df = pd.DataFrame(outtweets,columns=["id","created_at","favorite_count", "retweet_count", "text"])
df.to_csv('tweets/%s_tweets.csv' % keywords,index=False)
df.head(3)

