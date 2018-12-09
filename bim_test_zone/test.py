import tweepy

CONSUMER_KEY = "SnxpqkOeT0kNkVC6KRNZPb0fY"
CONSUMER_KEY_SECRET = "SN1Ld5PjarO3nJG3hSbemsxHPlKsy0DCi3osSCEM9Q0WHmcjUB"

ACCESS_TOKEN = "1481426107-ChPBgQwWUPZeTiAp0R5XwvMiDKp0JqasHv6yHH5"
ACCESS_TOKEN_SECRET = "q6E2XhGFYYBQGusbKL1L0SBms1sX9FlA2iEnbDvxEyNrU"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

public_tweets = api.search('trump')

for tweet in public_tweets :
	print(tweet.text)