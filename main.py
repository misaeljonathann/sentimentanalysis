from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import StreamListener
from tweepy import Stream
from pprint import pprint
import json
import tweepy

CONSUMER_KEY = "rg3GQNIK3uPviihUX9zR3ovbn"
CONSUMER_KEY_SECRET = "2BKF3652v6U4oU2mFnwtjx8zSSIpHyYvfMv4knG0xEStpgFNLT"

ACCESS_TOKEN = "1481426107-DYQFSEE5gNlRHG7fA1x1FgzVHQ3ZrPT1seFb23S"
ACCESS_TOKEN_SECRET = "RlbPOqAm5V8u0DD93l2qsizvFg05WLbyZqycPGFgYxbEz"

if __name__ == "__main__":

    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)
    track = "jokowi OR jkw OR jokowidodo OR"
    search = tweepy.Cursor(api.search, q=track, tweet_mode="extended").items(3200)

    with open('tweets.txt', 'w') as outfile:

        # TWEET EXTRACT
        for tweet_info in search:
            if 'retweeted_status' in dir(tweet_info):
                outfile.write(str(tweet_info.created_at) + " " + str((tweet_info.retweeted_status.full_text).encode("ascii", errors='ignore')) + "\n")
            else:
                outfile.write(str(tweet_info.created_at) + " " + str((tweet_info.full_text).encode("ascii", errors='ignore')) + "\n")    
        

