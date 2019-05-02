import tweepy
import pandas
import matplotlib.pyplot as plt
import seaborn as sns
import itertools
import collections
import nltk
from nltk.corpus import stopwords
import re
import networkx
import warnings


warnings.filterwarnings("ignore")


sns.set(font_scale = 1.5)
sns.set_style("whitegrid")

# definition des clés d'authentification

auth = tweepy.OAuthHandler("NLZ39ilLBflHHt8myenHdH3Ao", "FJ5EAa7DMtnrUHPFNXMuG0heucpzZPatYJNjoixFniWMK8WM0o")

auth.set_access_token("1117700066255474688-5BSckADfdnZTX1WAgTBQib1tnEXBMO", "eiTGX94V9NRpXr9cI5j29oR59MzVp1NeVhHNKCrl4xEWl")

api = tweepy.API(auth, wait_on_rate_limit = True)


search_term = "fortnite -filter:retweets"

tweets = tweepy.Cursor(api.search, q = search_term, lang = "en", since = '2019-04-01').items(50)

all_tweets = [tweet.text for tweet in tweets]

all_tweets[:5]

print(all_tweets)

all_tweets_without_url = [remove_url(tweet.text) for tweet in tweets]

all_tweets_without_url[:5]


def remove_url(txt):
    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())
