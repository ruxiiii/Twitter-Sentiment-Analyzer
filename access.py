import tweepy
from tweepy import OAuthHandler

consumer_key = "OJ4TDjEUDQISNba49vVrcev1u"
consumer_secret_key = "j2VTVxlgjEOR7nPYBBDQLVACcQhEVZs85bW5hvpl6VIljT0Ny2"
access_token = "1489302977269891072-VrPUsYpM6F6j6Zgy16srIb6zy7wZeo"
access_secret_token = "hj1JXPLtBHZzofJ46O0Ec7QIRmgNDxAv06iRy6m8d8ExY"
bearer_token = "AAAAAAAAAAAAAAAAAAAAABFNhQEAAAAA6Dlc5LCfDUYJmf27c3Hiel3PwKU%3DnnETTqE4wMFITwCt60QUVr4LcI6n7cuqmkXsqYhRwypOoKQDQS"


auth = OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_secret_token)

api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status.text)
