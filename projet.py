import sqlite3
import tweepy
import csv
import pandas as pd
import json
import codecs
import preprocessor as p
import textblob.exceptions
from sqlite3 import Error
from googletrans import Translator
import mtranslate
from textblob import TextBlob
import nltk
import time
from nltk.tokenize import word_tokenize
from nltk.tag import StanfordNERTagger
from unidecode import unidecode
import os

# ON REGLE LES CHEMINS DE DIRECTION

nltk.internals.config_java("C:/Program Files (x86)/Java/jre1.8.0_211/bin/java.exe")
java_path = "C:/Program Files (x86)/Java/jre1.8.0_211/bin/java.exe"
os.environ['JAVAHOME'] = java_path
st = StanfordNERTagger('C:/Users/TheoLC/Desktop/python/stanford/classifiers/english.all.3class.distsim.crf.ser.gz','C:/Users/TheoLC/Desktop/python/stanford/stanford-ner.jar',encoding='utf-8')

# FONCTIONS POUR SQLITE

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        print("Connecté a la base de données ! ")
    except Error as e:
        print(e)
    finally:
        conn.close()



def create_table(conn, create_table_sql):
    """
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        print("Table créée")
    except Error as e:
        print(e)

def insert_table(conn, sql):
    try:
        c = conn.cursor()
        c.executemany(sql)
        print("Requete acceptée")
    except Error as e:
        print(e)


def main():

    database = "C:\\Users\TheoLC\AppData\Local\Programs\Python\Python37\lib\sqlite3\pythonsqlite.db"

    try:
        conn = sqlite3.connect(database)
        print("Connecté a la base de données ! ")
    except Error as e:
        print(e)

    # IDENTIFICATION AVEC TOKENS TWITTER

    auth = tweepy.OAuthHandler("#", "#")

    auth.set_access_token("#-#", "#")

    api = tweepy.API(auth)

    translator = Translator()

    # ON DEMANDE LE MOT ET CELUI CI EST TRADUIT EN MULTIPLES LANGAGES

    search_word = input("subject ? \n")

    search_word = TextBlob(search_word)

    search_word_finnish = translator.translate(str(search_word), dest='fi')

    search_word_french = translator.translate(str(search_word), dest='fr')

    search_word_norwegian = translator.translate(str(search_word), dest='no')

    search_word_swedish = translator.translate(str(search_word), dest='sw')

    search_word_estonian = translator.translate(str(search_word), dest='et')

    search_word_russian = translator.translate(str(search_word), dest='ru')

    search_word_spanish = translator.translate(str(search_word), dest='es')

    print("Mot en finnois : " + str(search_word_finnish.text) + " \n")
    print("Mot en français : " + str(search_word_french.text) + " \n")
    print("Mot en norvégien : " + str(search_word_norwegian.text) + " \n")
    print("Mot en suédois : " + str(search_word_swedish.text) + " \n")
    print("Mot en estonien : " + str(search_word_estonian.text) + " \n")
    print("Mot en russe : " + str(search_word_russian.text) + " \n")
    print("Mot en espagnol : " + str(search_word_spanish.text) + " \n")

    searched_tweets = []

    # ON LANCE LA RECHERCHE DE TWEETS

    taille = input("nb de tweets ?")

    new_tweets_en = api.search(search_word, count=int(taille)/7)
    new_tweets_fi = api.search(search_word_finnish.text, count=int(taille)/7)
    new_tweets_fr = api.search(search_word_french.text, count=int(taille)/7)
    new_tweets_nr = api.search(search_word_norwegian.text, count=int(taille)/7)
    new_tweets_sw = api.search(search_word_swedish.text, count=int(taille)/7)
    new_tweets_et = api.search(search_word_estonian.text, count=int(taille)/7)
    new_tweets_ru = api.search(search_word_russian.text, count=int(taille)/7)
    new_tweets_es = api.search(search_word_spanish.text, count=int(taille)/7)

    print("j'ai trouver ", len(new_tweets_en), "tweets en anglais")
    print("j'ai trouver ", len(new_tweets_fi), "tweets en finnois")
    print("j'ai trouver ", len(new_tweets_fr), "tweets en français")
    print("j'ai trouver ", len(new_tweets_nr), "tweets en norvégien")
    print("j'ai trouver ", len(new_tweets_sw), "tweets en suédois")
    print("j'ai trouver ", len(new_tweets_et), "tweets en estonien")
    print("j'ai trouver ", len(new_tweets_ru), "tweets en russe")
    print("j'ai trouver ", len(new_tweets_es), "tweets en espagnol")



    if not new_tweets_en and not new_tweets_fr and not new_tweets_fi and not new_tweets_nr and not new_tweets_sw and not new_tweets_et and not new_tweets_ru and not new_tweets_es :
        print("pas de tweets trouves")

    new_tweets = new_tweets_en + new_tweets_fr + new_tweets_fi + new_tweets_nr + new_tweets_sw + new_tweets_et + new_tweets_ru + new_tweets_es
    searched_tweets.extend(new_tweets)

    # for tweet in new_tweets:
        # unidecode(tweet.text)
        # tweet.text = translator.translate(str(tweet.text), dest='en')


    # ON DELETE LE CONTENU DE LA TABLE

    c = conn.cursor()
    c.execute("DELETE FROM tweets")
    conn.commit()

    # ON INSERE LES TWEETS DANS LA BDD

    for tweet in searched_tweets:
        unidecode(tweet.text)
        c.execute("INSERT INTO tweets (id_tweet, username , content) VALUES (?, ?, ?);", (tweet.id, tweet.author.screen_name, tweet.text))
        conn.commit()
    print("Requete acceptée")

    # ON UTILISE L'ALGORITHME DE STANFORD

    for tweet in searched_tweets:
        unidecode(tweet.text) # on utilise unidecode pour eviter les erreurs d'encodage
        tokenized_text = word_tokenize(tweet.text) # algorithme de tokenization
        classified_text = st.tag(tokenized_text) # algorithme de stanford
        print(classified_text) # on l'affiche dans la console (très long)
        with open('data.txt','w') as outfile:
            json.dump(classified_text, outfile) # on le stocke dans un fichier json
            print("tweet classé par stanford")
    print("STANFORD ACCOMPLI")

if __name__ == "__main__":
    main()
