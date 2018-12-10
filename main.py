from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import StreamListener
from tweepy import Stream
from pprint import pprint
import json
import tweepy

CONSUMER_KEY = "SnxpqkOeT0kNkVC6KRNZPb0fY"
CONSUMER_KEY_SECRET = "SN1Ld5PjarO3nJG3hSbemsxHPlKsy0DCi3osSCEM9Q0WHmcjUB"

ACCESS_TOKEN = "1481426107-ChPBgQwWUPZeTiAp0R5XwvMiDKp0JqasHv6yHH5"
ACCESS_TOKEN_SECRET = "q6E2XhGFYYBQGusbKL1L0SBms1sX9FlA2iEnbDvxEyNrU"

if __name__ == "__main__":

    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)
    track = "prabowo"
    search = tweepy.Cursor(api.search, q=track, tweet_mode="extended").items(3200)
    
    with open('tweets2.txt', 'w') as outfile:

        # TWEET EXTRACT
        for tweet_info in search:
            if 'retweeted_status' in dir(tweet_info):
                outfile.write(str(tweet_info.created_at) + " " + str((tweet_info.retweeted_status.full_text).encode("ascii", errors='ignore')) + "\n")
            else:
                outfile.write(str(tweet_info.created_at) + " " + str((tweet_info.full_text).encode("ascii", errors='ignore')) + "\n")    
        
        # USER EXTRACT
        # for status in tweepy.Cursor(api.user_timeline, screen_name="@susipudjiastuti", count=10000, tweet_mode="extended").items():
        #     outfile.write(str(status.created_at) + " => " + str((status.full_text).encode("utf-8")) + "\n")


