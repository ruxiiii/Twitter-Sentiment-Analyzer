import tweepy

consumer_key = "OJ4TDjEUDQISNba49vVrcev1u"
consumer_secret_key = "j2VTVxlgjEOR7nPYBBDQLVACcQhEVZs85bW5hvpl6VIljT0Ny2"
access_token = "1489302977269891072-VrPUsYpM6F6j6Zgy16srIb6zy7wZeo"
access_secret_token = "hj1JXPLtBHZzofJ46O0Ec7QIRmgNDxAv06iRy6m8d8ExY"
bearer_token = "AAAAAAAAAAAAAAAAAAAAABFNhQEAAAAA6Dlc5LCfDUYJmf27c3Hiel3PwKU%3DnnETTqE4wMFITwCt60QUVr4LcI6n7cuqmkXsqYhRwypOoKQDQS"


auth_handler = tweepy.OAuthHandler(
    consumer_key=consumer_key, consumer_secret=consumer_secret_key
)
auth_handler.set_access_token(access_token, access_secret_token)

api = tweepy.API(auth_handler)

search_item = "cyrpto"
tweet_amount = 10

tweets = tweepy.Cursor(api.search_tweets, q=search_item, lang="en").items(tweet_amount)

for tweet in tweets:
    print(tweet.text)


import tweepy

consumer_key = "OJ4TDjEUDQISNba49vVrcev1u"
consumer_secret_key = "j2VTVxlgjEOR7nPYBBDQLVACcQhEVZs85bW5hvpl6VIljT0Ny2"
access_token = "1489302977269891072-VrPUsYpM6F6j6Zgy16srIb6zy7wZeo"
access_secret_token = "hj1JXPLtBHZzofJ46O0Ec7QIRmgNDxAv06iRy6m8d8ExY"
bearer_token = "AAAAAAAAAAAAAAAAAAAAABFNhQEAAAAA6Dlc5LCfDUYJmf27c3Hiel3PwKU%3DnnETTqE4wMFITwCt60QUVr4LcI6n7cuqmkXsqYhRwypOoKQDQS"

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret_key, access_token, access_secret_token
)
api = tweepy.API(auth)
user = api.get_user(screen_name="realDonaldTrump")
print(user)


# Tweepy Package
import tweepy

# Connecting to the API
consumer_key = "OJ4TDjEUDQISNba49vVrcev1u"
consumer_secret_key = "j2VTVxlgjEOR7nPYBBDQLVACcQhEVZs85bW5hvpl6VIljT0Ny2"
access_token = "1489302977269891072-VrPUsYpM6F6j6Zgy16srIb6zy7wZeo"
access_secret_token = "hj1JXPLtBHZzofJ46O0Ec7QIRmgNDxAv06iRy6m8d8ExY"
bearer_token = "AAAAAAAAAAAAAAAAAAAAABFNhQEAAAAA6Dlc5LCfDUYJmf27c3Hiel3PwKU%3DnnETTqE4wMFITwCt60QUVr4LcI6n7cuqmkXsqYhRwypOoKQDQS"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_secret_token)
api = tweepy.API(auth)
# Accessing my account information
user = api.get_user(screen_name="SahilBloom")
print(user)
