import tweepy
import access

client = tweepy.Client(access.bearer_token)


class stdOutListener(tweepy.StreamingClient):
    def on_data(self, raw_data):
        return super().on_data(raw_data)

    def on_errors(self, errors):
        return super().on_errors(errors)


if __name__ == "__main__":
    listener = stdOutListener(client)
    listener.filter(
        track=["donald trump", "hillary clinton", "barack obama", "bernie sanders"]
    )

