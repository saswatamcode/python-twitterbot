import tweepy
from time import sleep
from twitterbot_credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search,q='#code').items(10):
    try:
        print('\nTweet by: @' + tweet.user.screen_name)
        tweet.retweet()
        print('Retweeted the tweet')
        tweet.favorite()
        print('Favorited the tweet')

        tweet.user.follow()
        print('Followed the user')
        sleep(5)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
