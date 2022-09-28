from tweepy import OAuthHandler
from tweepy import Stream

import access


class StdOutListener(Stream):
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == "__main__":

    listener = StdOutListener(
        access.consumer_key,
        access.consumer_secret_key,
        access.access_token,
        access.access_secret_token,
    )

    listener.filter(
        track=["donald trump", "hillary clinton", "barack obama", "bernie sanders"]
    )

