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

# class StdOutListener(StreamListener):
#     def __init__(self):
#         self.counter = 0
#         self.limit = 10

#     def on_data(self, data):
#         json_data = json.dumps(self.data)
#         val = json.dumps(data, indent=4)
#         decode = json.loads(val)

#         with open('data.json', 'w') as outfile:
#             json.dump(data, outfile)
#         if self.counter == self.limit :
#             return False
#         self.counter = self.counter + 1
        
#         return True
    
#     def on_error(self, status):
#         print(status)

if __name__ == "__main__":
    # listener = StdOutListener()
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)
    track = "jokowi OR jkw OR jokowidodo"
    search = tweepy.Cursor(api.search, q=track, tweet_mode="extended").items(20)
    
    with open('tweets.txt', 'w') as outfile:
        
        # TWEET EXTRACT
        for item in search:
            outfile.write(str(item.created_at) + " " + str((item.full_text).encode("ascii", errors='ignore')) + "\n")
        
        # USER EXTRACT
        # for status in tweepy.Cursor(api.user_timeline, screen_name="@susipudjiastuti", count=10000, tweet_mode="extended").items():
        #     outfile.write(str(status.created_at) + " => " + str((status.full_text).encode("utf-8")) + "\n")


    # stream = Stream(auth, listener)
    # stream.filter(track=['jokowi dodo', 'jokowi', 'jkw', 'jokowidodo'])

