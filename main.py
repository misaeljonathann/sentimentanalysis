from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import StreamListener
from tweepy import Stream
import json

CONSUMER_KEY = "SnxpqkOeT0kNkVC6KRNZPb0fY"
CONSUMER_KEY_SECRET = "SN1Ld5PjarO3nJG3hSbemsxHPlKsy0DCi3osSCEM9Q0WHmcjUB"

ACCESS_TOKEN = "1481426107-ChPBgQwWUPZeTiAp0R5XwvMiDKp0JqasHv6yHH5"
ACCESS_TOKEN_SECRET = "q6E2XhGFYYBQGusbKL1L0SBms1sX9FlA2iEnbDvxEyNrU"

class StdOutListener(StreamListener):
    def __init__(self):
        self.counter = 0
        self.limit = 10
    def on_data(self, data):
        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)
        if self.counter == self.limit :
            return False
        self.counter = self.counter + 1
        return True
    
    def on_error(self, status):
        print(status)

if __name__ == "__main__":
    listener = StdOutListener()
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    stream = Stream(auth, listener)

    stream.filter(track=['jokowi dodo', 'jokowi', 'jkw', 'jokowidodo'])

