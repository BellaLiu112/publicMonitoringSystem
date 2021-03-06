import tweepy
from tweepy import OAuthHandler
import json
import time
import re
import os
import random
from util import rand_file_name
from util import mkdirs
from util import is_blank_line
from util import clear_url
import sys

consumer_key = 'CDq4zm9Gu5A07KakkYyIviMYn'
consumer_secret = 'PVUgtdj7FC6xkKPMRBZ1cjB8xQ86EcCWFLiQJP2UUaReFJSqA9'
access_token = '7939525151602774016-wmIukaGwjopWCz4ebAvGjmJD9I4YbJA'
access_secret = 'SNHNLDftRySr5gln7sbANjIJzF7wTEP2k4xqe71Z2CYZi'

auth = OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

#target_name = 'alibaba'
#extra_key_words = ['alibaba']
target_name = sys.argv[1]
extra_key_words = [sys.argv[1]]
file_path = target_name + '/' + time.strftime('%Y-%m-%d-%M',time.localtime(time.time()))
mkdirs(file_path)

max_text_count = 500
current_text_count = 0


def process_full_text(full_text):
    global current_text_count

    # skip short text
    size = len(full_text)
    if size <= 2:
        return

    # clear url
    full_text = clear_url(full_text)
    # it may be a blank line while url was cleared
    if is_blank_line(full_text):
        return

    # write to file

    file_name = rand_file_name(file_path)
    file = open(file_name, 'w')
    file.write(full_text)
    file.close()

    if current_text_count >= max_text_count:
        twitterStream.disconnect()
    else:
        current_text_count = current_text_count + 1


class MyStreamListener(tweepy.StreamListener):
    def on_data(self, raw_data):
        data = json.loads(raw_data)
        if 'extended_tweet' in data:
            extended_tweet = data['extended_tweet']
            if 'full_text' in extended_tweet:
                full_text = extended_tweet['full_text']
                process_full_text(full_text)

    def on_error(self, status_code):
        print(status_code)


if __name__ == '__main__':
    listener = MyStreamListener()
    twitterStream = tweepy.Stream(auth = auth, listener = listener)
    tracks = extra_key_words
    twitterStream.filter(track = tracks)
