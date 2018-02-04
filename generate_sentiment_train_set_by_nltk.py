import os
from nltk import tokenize
import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import random
from util import mkdirs
from util import rand_file_name
from util import clear_emoji

sid = SentimentIntensityAnalyzer()


def generate_sentiment_train_set(src_dir,test_dir):

    mkdirs(test_dir)
    pos_dir = test_dir + '/pos'
    mkdirs(pos_dir)
    neg_dir = test_dir + '/neg'
    mkdirs(neg_dir)
    neu_dir = test_dir + '/neu'
    mkdirs(neu_dir)

    for item in os.listdir(src_dir):
        if item[0] =='.': #.Ds_store
            continue
        file = open(src_dir + '/' + item)
        content = file.read()
        file.close()

        sentence = clear_emoji(content)
        ss = sid.polarity_scores(sentence)
        ss.pop('compound')
        sentiment = max(ss, key=lambda x: ss[x])

        filtered_file_path = rand_file_name(test_dir + '/' + sentiment)
        filtered_file = open(filtered_file_path, 'w')
        filtered_file.write(content)
        filtered_file.close()

if __name__ == '__main__':
    #通过nltk对抓取数据进行处理已获取训练数据
    generate_sentiment_train_set("facebook/2017-12-100.3532025204309708", "test_facebook")
    generate_sentiment_train_set("facebook/2017-12-100.4001048715529565", "test_facebook")
    generate_sentiment_train_set("facebook/2017-12-100.6833095791970586", "test_facebook")
    generate_sentiment_train_set("facebook/2017-12-100.8867056463298973", "test_facebook")
    generate_sentiment_train_set("facebook/2017-12-100.23590662055554723","test_facebook")

    #generate_sentiment_train_set("trump/2017-12-10-33","trump_test")
    #generate_sentiment_train_set("trump/2017-12-10-40", "trump_test")
