#!/usr/bin/python
from sys import stdout
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import json
import time
import redis

# Establish the connection with Redis first to avoid multiple connections.
global conn
conn = redis.Redis()

# Initialize the "last_time" to record the timestamp of last tweet.
global last_time
last_time = 0


def main():
    # Authentication information for Twitter API
    consumer_key = ""
    consumer_secret = ""
    access_token = ""
    access_key = ""

    # Setup the authentication handler of Twitter API
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_key)

    # Start the real_time streaming from twitter, which calls the modified Listener Class at the bottom
    twitter_stream = Stream(auth, Listener())

    # This filter limits the tweets from the following location, a rectangle that covers the Great New York Area,
    # where latitude ranges from 40 to 42 and longitude ranges from -71 to -75.
    twitter_stream.filter(locations=[-75, 40, -71, 42], async=False)


class Listener(StreamListener):

    # This methods overrides the existing one, which will be run once a new tweet is captured.
    def on_data(self, data):
        global conn
        global last_time

        # Use JSON to parse received data, which contains multiple information of the tweet.
        received_data = json.loads(data)
        try:
            # Print the "lat" and "lng" out to be read by Websocketd.
            print json.dumps({'lat': received_data['geo']['coordinates'][0],
                              'lng': received_data['geo']['coordinates'][1]})

            # Initialize last time for the first loop
            if last_time == 0:
                last_time = time.time()

            # Calculate the time difference between this tweet and the previous one
            delta_time = time.time() - last_time

            # Store time of now for the next loop
            last_time = time.time()

            # Send time and time difference to Redis, keep it on Redis for 600 seconds
            conn.setex(last_time, delta_time, 600)
            stdout.flush()
        except:
            pass
        return True

    def on_error(self, status):
        print status


if __name__ == "__main__":
    main()
