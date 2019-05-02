import tweepy
import csv
import pandas
import json
from googletrans import Translator
import codecs
import preprocessor as p
import textblob.exceptions
from textblob import TextBlob
import nltk
from nltk.tokenize import word_tokenize

auth = tweepy.OAuthHandler("NLZ39ilLBflHHt8myenHdH3Ao", "FJ5EAa7DMtnrUHPFNXMuG0heucpzZPatYJNjoixFniWMK8WM0o")

auth.set_access_token("1117700066255474688-5BSckADfdnZTX1WAgTBQib1tnEXBMO", "eiTGX94V9NRpXr9cI5j29oR59MzVp1NeVhHNKCrl4xEWl")

api = tweepy.API(auth)

search_word = input("subject ? \n")

search_word = TextBlob(search_word)

search_word_detect = search_word.detect_language()

search_word_finnish = search_word.translate(from_lang = search_word_detect, to='fi')

search_word_french = search_word.translate(from_lang = search_word_detect, to='fr')


searched_tweets = []

taille = input("nb de tweets ?")

new_tweets_en = api.search(search_word, count=int(taille)/3)
new_tweets_fi = api.search(search_word_finnish, count=int(taille)/3)
new_tweets_fr = api.search(search_word_french, count=int(taille)/3)


print("j'ai trouver ", len(new_tweets_en), "tweets en anglais")
print("j'ai trouver ", len(new_tweets_fi), "tweets en finnois")
print("j'ai trouver ", len(new_tweets_fr), "tweets en français")

if not new_tweets_en and not new_tweets_fi and not new_tweets_fr:
    print("pas de tweets trouves")

new_tweets = new_tweets_en + new_tweets_fi + new_tweets_fr
searched_tweets.extend(new_tweets)

out_tweets = [[tweet.text.encode("utf-8-sig")] for tweet in new_tweets]


with codecs.open("%s_tweets.csv" % search_word, 'a', "utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(out_tweets)

