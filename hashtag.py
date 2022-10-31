
import tweepy
import pandas as pd



consumer_key = 'Wc46qw5CVy9JQ2DOzgIlYkKlG'
consumer_secret = 'sNTQZl18KGowmHDHFJqPgJoq8M3SVtGe8RY1UY6ztr9yl8lNAs'
access_token = '1584651535933267968-Iq8u3WDEFTGV4IVzoETufQGDGPnwh0'
access_token_secret = 'wHqPJ0eLir3OjopC2MPey7S6cKOLux2Z4TYMfZCdu9K6z'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

userID = "SenToniAtkins"

tweets = api.user_timeline(screen_name=userID, 
                           # 200 is the maximum allowed count
                           count=200,
                           include_rts = False,
                           # Necessary to keep full_text 
                           # otherwise only the first 140 words are extracted
                           tweet_mode = 'extended'
                           )

for info in tweets[:3]:
    print("ID: {}".format(info.id))
    print(info.created_at)
    print(info.full_text.encode('utf-8'))
    print("\n")

all_tweets = []
all_tweets.extend(tweets)
oldest_id = tweets[-1].id
while True:
    tweets = api.user_timeline(screen_name=userID, 
                           # 200 is the maximum allowed count
                           count=200,
                           include_rts = False,
                           max_id = oldest_id - 1,
                           # Necessary to keep full_text 
                           # otherwise only the first 140 words are extracted
                           tweet_mode = 'extended'
                           )
    if len(tweets) == 0:
        break
    oldest_id = tweets[-1].id
    all_tweets.extend(tweets)
    print('N of tweets downloaded till now {}'.format(len(all_tweets)))


outtweets = [[tweet.id_str, 
            tweet.created_at, 
            tweet.favorite_count, 
            tweet.retweet_count, 
            tweet.full_text.encode("utf-8").decode("utf-8")] 
            for idx,tweet in enumerate(all_tweets)]
df = pd.DataFrame(outtweets,columns=["id","created_at","favorite_count","retweet_count", "text"])
df.to_csv('%s_tweets.csv' % userID,index=False)
df.head(3)