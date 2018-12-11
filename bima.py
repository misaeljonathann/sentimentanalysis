from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import StreamListener
from tweepy import Stream
from pprint import pprint
import json
import tweepy

CONSUMER_KEY = "UUCxBb6SVN4uENYuXOVCigNYg"
CONSUMER_KEY_SECRET = "QA7YMhVUJ7x5muQt0SW4Pts9sg4L1TZVLbMELaG7eAO94F6EtN"

ACCESS_TOKEN = "890682047601098753-x1kSBNLehFMO2ornerKnYlX8EHMwvLj"
ACCESS_TOKEN_SECRET = "M6AHh6iceDZFZIipVd53dY6T17bT0BBNeeP3lapoW0XIU"

if __name__ == "__main__":

    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)
    track = "prabowo"
    search = tweepy.Cursor(api.search, q=track, tweet_mode="extended").items(3200)
    
    with open('tweets_prab.txt', 'a') as outfile:

        # TWEET EXTRACT
        for tweet_info in search:
            if 'retweeted_status' in dir(tweet_info):
                outfile.write(str(tweet_info.created_at) + " " + str((tweet_info.retweeted_status.full_text).encode("ascii", errors='ignore')) + "\n")
            else:
                outfile.write(str(tweet_info.created_at) + " " + str((tweet_info.full_text).encode("ascii", errors='ignore')) + "\n")    
        
        # USER EXTRACT
        # for status in tweepy.Cursor(api.user_timeline, screen_name="@susipudjiastuti", count=10000, tweet_mode="extended").items():
        #     outfile.write(str(status.created_at) + " => " + str((status.full_text).encode("utf-8")) + "\n")


