# PARTIE IMPORTATION

import tweepy
import os
import nltk
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize


# ON REGLE LES CHEMINS DE DIRECTION

nltk.internals.config_java("C:/Program Files (x86)/Java/jre1.8.0_211/bin/java.exe")
java_path = "C:/Program Files (x86)/Java/jre1.8.0_211/bin/java.exe"
os.environ['JAVAHOME'] = java_path
st = StanfordNERTagger('C:/Users/TheoLC/Desktop/python/stanford/classifiers/english.all.3class.distsim.crf.ser.gz','C:/Users/TheoLC/Desktop/python/stanford/stanford-ner.jar',encoding='utf-8')



# ON S'AUTHENTIFIE API TWITTER

auth = tweepy.OAuthHandler("NLZ39ilLBflHHt8myenHdH3Ao", "FJ5EAa7DMtnrUHPFNXMuG0heucpzZPatYJNjoixFniWMK8WM0o")
auth.set_access_token("1117700066255474688-5BSckADfdnZTX1WAgTBQib1tnEXBMO", "eiTGX94V9NRpXr9cI5j29oR59MzVp1NeVhHNKCrl4xEWl")
api = tweepy.API(auth, wait_on_rate_limit = True)

# VIF DU SUJET

search_word = input("entrer le mot que vous chercher : ")

date_since = "2019-04-01"

tweets = tweepy.Cursor(api.search, q = search_word, lang = "en", since = date_since).items(1)

tweets_text = [[tweet.text] for tweet in tweets]

data_final = str(tweets_text)

tokenized_text = word_tokenize(data_final) # On divise la phrase morceau par morceau, en tokens
classified_text = st.tag(tokenized_text)

print(classified_text)
