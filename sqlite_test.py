import sqlite3
import tweepy
import json
import matplotlib.pyplot as plt
import codecs
import pandas as pd
import csv
import textblob.exceptions
from sqlite3 import Error
from googletrans import Translator
from textblob import TextBlob
import nltk
import time
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from unidecode import unidecode
import gensim
import logging
import tempfile
import os
from gensim import corpora, models, similarities
import pyLDAvis.gensim
import IPython.core

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


def main():

    database = "C:\\Users\TheoLC\AppData\Local\Programs\Python\Python37\lib\sqlite3\pythonsqlite.db"

    try:
        conn = sqlite3.connect(database)
        print("Connecté a la base de données ! \n")

    except Error as e:
        print(e)


    # IDENTIFICATION AVEC TOKENS TWITTER

    auth = tweepy.OAuthHandler("NLZ39ilLBflHHt8myenHdH3Ao", "FJ5EAa7DMtnrUHPFNXMuG0heucpzZPatYJNjoixFniWMK8WM0o")

    auth.set_access_token("1117700066255474688-5BSckADfdnZTX1WAgTBQib1tnEXBMO", "eiTGX94V9NRpXr9cI5j29oR59MzVp1NeVhHNKCrl4xEWl")

    api = tweepy.API(auth)

    translate_urls = ["translate.google.com", "translate.google.co.kr",
                      "translate.google.at", "translate.google.de",
                      "translate.google.ru", "translate.google.ch",
                      "translate.google.fr", "translate.google.es"]

    translator = Translator(service_urls = translate_urls)

    # ON RECHERCHE LE MOT ET CELUI CI EST TRADUIT EN MULTIPLES LANGAGES

    print("Recherche de tweets sur les futures élections finlandaises")

    search_word = TextBlob("élections finlandaises")

    search_word2 = TextBlob("presidentin äänestys")

    search_word3 = TextBlob("presidentin valinta")
    
    search_word4 = TextBlob("finnish elections")

    search_word_finnish = translator.translate(str(search_word), dest='fi')

    print("Mot en finnois : " + str(search_word_finnish.text) + " \n")

    searched_tweets = []

    # ON LANCE LA RECHERCHE DE TWEETS

    new_tweets_fi2 = api.search(search_word2, count=400)
    new_tweets_fi3 = api.search(search_word3, count=400)
    new_tweets_fi = api.search(search_word_finnish.text, count=400)

    new_tweets_fi = new_tweets_fi + new_tweets_fi2 + new_tweets_fi3

    print("j'ai trouver ", len(new_tweets_fi), "tweets en finnois sur les élections finlandaises \n")

    print("recherche des principaux partis finlandais : \n")

    parti1 = api.get_user('Demarit')

    print("Parti trouvé : " + parti1.name + "\n")
    print("Localisation de " + parti1.name + " : " + str(parti1.location) + "\n")
    print("Nombre d'abonnés de " + parti1.name + " : " + str(parti1.followers_count) + "\n")
    print("__________________________________________________________________________________ \n")

    parti2 = api.get_user('keskusta')

    print("Parti trouvé : " + parti2.name + "\n")
    print("Localisation de " + parti2.name + " : " + str(parti2.location) + "\n")
    print("Nombre d'abonnés de " + parti2.name + " : " + str(parti2.followers_count) + "\n")
    print("__________________________________________________________________________________ \n")

    parti3 = api.get_user('kokoomus')

    print("Parti trouvé : " + parti3.name + "\n")
    print("Localisation de " + parti3.name + " : " + str(parti3.location) + "\n")
    print("Nombre d'abonnés de " + parti3.name + " : " + str(parti3.followers_count) + "\n")
    print("__________________________________________________________________________________ \n")


    parti4 = api.get_user('KDpuolue')

    print("Parti trouvé : " + parti4.name + "\n")
    print("Localisation de " + parti4.name + " : " + str(parti4.location) + "\n")
    print("Nombre d'abonnés de " + parti4.name + " : " + str(parti4.followers_count) + "\n")
    print("__________________________________________________________________________________ \n")

    parti5 = api.get_user('persut')

    print("Parti trouvé : " + parti5.name + "\n")
    print("Localisation de " + parti5.name + " : " + str(parti5.location) + "\n")
    print("Nombre d'abonnés de " + parti5.name + " : " + str(parti5.followers_count) + "\n")
    print("__________________________________________________________________________________ \n")

    parti6 = api.get_user('SiniTulevaisuus')

    print("Parti trouvé : " + parti6.name + "\n")
    print("Localisation de " + parti6.name + " : " + str(parti6.location) + "\n")
    print("Nombre d'abonnés de " + parti6.name + " : " + str(parti6.followers_count) + "\n")
    print("__________________________________________________________________________________ \n")

    parti7 = api.get_user('sfprkp')

    print("Parti trouvé : " + parti7.name + "\n")
    print("Localisation de " + parti7.name + " : " + str(parti7.location) + "\n")
    print("Nombre d'abonnés de " + parti7.name + " : " + str(parti7.followers_count) + "\n")
    print("__________________________________________________________________________________ \n")


    parti8 = api.get_user('vasemmisto')

    print("Parti trouvé : " + parti8.name + "\n")
    print("Localisation de " + parti8.name + " : " + str(parti8.location) + "\n")
    print("Nombre d'abonnés de " + parti8.name + " : " + str(parti8.followers_count) + "\n")
    print("__________________________________________________________________________________ \n")

    parti9 = api.get_user('vihreat')

    print("Parti trouvé : " + parti9.name + "\n")
    print("Localisation de " + parti9.name + " : " + str(parti9.location) + "\n")
    print("Nombre d'abonnés de " + parti9.name + " : " + str(parti9.followers_count) + "\n")
    print("__________________________________________________________________________________ \n")


    parti1_tweets = api.user_timeline(screen_name='Demarit', count=400, include_rts = True)
    parti2_tweets = api.user_timeline(screen_name='keskusta', count=400, include_rts = True)
    parti3_tweets = api.user_timeline(screen_name='kokoomus', count=400, include_rts = True)
    parti4_tweets = api.user_timeline(screen_name='KDpuolue', count=400, include_rts = True)
    parti5_tweets = api.user_timeline(screen_name='persut', count=400, include_rts = True)
    parti6_tweets = api.user_timeline(screen_name='SiniTulevaisuus', count=400, include_rts = True)
    parti7_tweets = api.user_timeline(screen_name='sfprkp', count=400, include_rts = True)
    parti8_tweets = api.user_timeline(screen_name='vasemmisto', count=400, include_rts = True)
    parti9_tweets = api.user_timeline(screen_name='vihreat', count=400, include_rts = True)

    print("Recherche des leaders de chaque parti : \n")

    leader_parti1 = api.get_user('AnttiRinnepj')

    print("Nom du leader du parti Demarit : " + leader_parti1.name + "\n")
    print("Nombre d'abonnés : " + str(leader_parti1.followers_count) + "\n")

    leader_parti2 = api.get_user('juhasipila')

    print("Nom du leader du parti Keskusta : " + leader_parti2.name + "\n")
    print("Nombre d'abonnés : " + str(leader_parti2.followers_count) + "\n")

    leader_parti3 = api.get_user('PetteriOrpo')

    print("Nom du leader du parti Kokoomus : " + leader_parti3.name + "\n")
    print("Nombre d'abonnés : " + str(leader_parti3.followers_count) + "\n")

    leader_parti4 = api.get_user('SariEssayah')

    print("Nom du leader du parti KDpuolue : " + leader_parti4.name + "\n")
    print("Nombre d'abonnés : " + str(leader_parti4.followers_count) + "\n")

    leader_parti5 = api.get_user('Halla_aho')

    print("Nom du leader du parti Persut : " + leader_parti5.name + "\n")
    print("Nombre d'abonnés : " + str(leader_parti5.followers_count) + "\n")

    leader_parti6 = api.get_user('Simon_Elo')

    print("Nom du leader du parti SiniTulevaisuus : " + leader_parti6.name + "\n")
    print("Nombre d'abonnés : " + str(leader_parti6.followers_count) + "\n")

    leader_parti7 = api.get_user('anna_maja')

    print("Nom du leader du parti sfprkp : " + leader_parti7.name + "\n")
    print("Nombre d'abonnés : " + str(leader_parti7.followers_count) + "\n")

    leader_parti8 = api.get_user('liandersson')

    print("Nom du leader du parti vasemmisto : " + leader_parti8.name + "\n")
    print("Nombre d'abonnés : " + str(leader_parti8.followers_count) + "\n")

    leader_parti9 = api.get_user('Haavisto')

    print("Nom du leader du parti vihreat : " + leader_parti9.name + "\n")
    print("Nombre d'abonnés : " + str(leader_parti9.followers_count) + "\n")

    leader_parti1_tweets = api.user_timeline(screen_name='AnttiRinnepj', count=400, include_rts = True)
    leader_parti2_tweets = api.user_timeline(screen_name='juhasipila', count=400, include_rts = True)
    leader_parti3_tweets = api.user_timeline(screen_name='PetteriOrpo', count=400, include_rts = True)
    leader_parti4_tweets = api.user_timeline(screen_name='SariEssayah', count=400, include_rts = True)
    leader_parti5_tweets = api.user_timeline(screen_name='Halla_aho', count=400, include_rts = True)
    leader_parti6_tweets = api.user_timeline(screen_name='Simon_Elo', count=400, include_rts = True)
    leader_parti7_tweets = api.user_timeline(screen_name='anna_maja', count=400, include_rts = True)
    leader_parti8_tweets = api.user_timeline(screen_name='liandersson', count=400, include_rts = True)
    leader_parti9_tweets = api.user_timeline(screen_name='Haavisto', count=400, include_rts = True)

    viceleader_parti1_tweets = api.user_timeline(screen_name='AnttiLindtman', count=400, include_rts = True)
    viceleader2_parti1_tweets = api.user_timeline(screen_name='MarinSanna', count=400, include_rts = True)
    viceleader3_parti1_tweets = api.user_timeline(screen_name='KristaKiuru', count=400, include_rts = True)

    viceleaders_partiDemarit_tweets = viceleader_parti1_tweets + viceleader2_parti1_tweets + viceleader3_parti1_tweets

    viceleader_parti2_tweets = api.user_timeline(screen_name='JuhaRehula', count=400, include_rts = True)
    viceleader2_parti2_tweets = api.user_timeline(screen_name='AnnikaSaarikko', count=400, include_rts = True)
    viceleader3_parti2_tweets = api.user_timeline(screen_name='AnuVehvilainen', count=400, include_rts = True)

    viceleaders_partiKeskusta_tweets = viceleader_parti2_tweets + viceleader2_parti2_tweets + viceleader3_parti2_tweets

    viceleader_parti3_tweets = api.user_timeline(screen_name='AMVirolainen', count=400, include_rts = True)
    viceleader2_parti3_tweets = api.user_timeline(screen_name='sannigrahn', count=400, include_rts = True)
    viceleader3_parti3_tweets = api.user_timeline(screen_name='JanneSankelo', count=400, include_rts = True)

    viceleaders_partiKokoomus_tweets = viceleader_parti3_tweets + viceleader2_parti3_tweets + viceleader3_parti3_tweets    

    viceleader_parti5_tweets = api.user_timeline(screen_name='LauraHuhtasaari', count=400, include_rts = True)

    viceleader_parti8_tweets = api.user_timeline(screen_name='joonasleppan', count=400, include_rts = True)
    

    new_tweets = new_tweets_fi
    searched_tweets.extend(new_tweets)


    # ON DELETE LE CONTENU DE LA TABLE

    print("suppression du contenu des tables")
    c = conn.cursor()
    c.execute("DELETE FROM tweets")
    c.execute("DELETE FROM tweets_by_Keskusta")
    c.execute("DELETE FROM tweets_by_Kokoomus")
    c.execute("DELETE FROM tweets_by_Demarit")
    c.execute("DELETE FROM tweets_by_KDpuolue")
    c.execute("DELETE FROM tweets_by_Persut")
    c.execute("DELETE FROM tweets_by_SiniTulevaisuus")
    c.execute("DELETE FROM tweets_by_sfprkp")
    c.execute("DELETE FROM tweets_by_vasemmisto")
    c.execute("DELETE FROM tweets_by_vihreat")
    c.execute("DELETE FROM tweets_by_leader_Keskusta")
    c.execute("DELETE FROM tweets_by_leader_Kokoomus")
    c.execute("DELETE FROM tweets_by_leader_Demarit")
    c.execute("DELETE FROM tweets_by_leader_KDpuolue")
    c.execute("DELETE FROM tweets_by_leader_Persut")
    c.execute("DELETE FROM tweets_by_leader_SiniTulevaisuus")
    c.execute("DELETE FROM tweets_by_leader_sfprkp")
    c.execute("DELETE FROM tweets_by_leader_vasemmisto")
    c.execute("DELETE FROM tweets_by_leader_vihreat")
    c.execute("DELETE FROM tweets_viceleaders_Demarit")
    c.execute("DELETE FROM tweets_viceleaders_Keskusta")
    c.execute("DELETE FROM tweets_viceleaders_Kokoomus")
    c.execute("DELETE FROM tweets_viceleaders_parti5")
    c.execute("DELETE FROM tweets_viceleaders_parti8")

    conn.commit()

    # ON INSERE LES TWEETS DANS LA BDD

    print("INSERTION DES TWEETS EN RAPPORT AVEC LES ELECTIONS FINLANDAISES \n \n")

    for tweet in searched_tweets:
        unidecode(tweet.text)
        c.execute("INSERT OR IGNORE INTO tweets (id_tweet, username , content) VALUES (?, ?, ?);", (tweet.id, tweet.author.screen_name, tweet.text))
        conn.commit()
    print("Requete acceptée pour la table tweets")

    ###################################

    print("INSERTION DES TWEETS DES PARTIS \n \n")

    for tweet in parti2_tweets:
        unidecode(tweet.text)
        c.execute("INSERT OR IGNORE INTO tweets_by_Keskusta (id_tweet, content) VALUES (?, ?);", (tweet.id, tweet.text))
        conn.commit()
    print("Requete acceptée pour le parti Keskusta")

    for tweet in parti3_tweets:
        unidecode(tweet.text)
        c.execute("INSERT OR IGNORE INTO tweets_by_Kokoomus (id_tweet, content) VALUES (?, ?);", (tweet.id, tweet.text))
        conn.commit()
    print("Requete acceptée pour le parti Kokoomus")

    for tweet in parti1_tweets:
        unidecode(tweet.text)
        c.execute("INSERT OR IGNORE INTO tweets_by_Demarit (id_tweet, content) VALUES (?, ?);", (tweet.id, tweet.text))
        conn.commit()
    print("Requete acceptée pour le parti Demarit")

    for tweet in parti4_tweets:
        unidecode(tweet.text)
        c.execute("INSERT OR IGNORE INTO tweets_by_KDpuolue (id_tweet, content) VALUES (?, ?);", (tweet.id, tweet.text))
        conn.commit()
    print("Requete acceptée pour le parti KDpuolue")

    for tweet in parti5_tweets:
        unidecode(tweet.text)
        c.execute("INSERT OR IGNORE INTO tweets_by_Persut (id_tweet, content) VALUES (?, ?);", (tweet.id, tweet.text))
        conn.commit()
    print("Requete acceptée pour le parti Persut")

    for tweet in parti6_tweets:
        unidecode(tweet.text)
        c.execute("INSERT OR IGNORE INTO tweets_by_SiniTulevaisuus (id_tweet, content) VALUES (?, ?);", (tweet.id, tweet.text))
        conn.commit()
    print("Requete acceptée pour le parti SiniTulevaisuus")

    for tweet in parti7_tweets:
        unidecode(tweet.text)
        c.execute("INSERT OR IGNORE INTO tweets_by_sfprkp (id_tweet, content) VALUES (?, ?);", (tweet.id, tweet.text))
        conn.commit()
    print("Requete acceptée pour le parti sfprkp")

    for tweet in parti8_tweets:
        unidecode(tweet.text)
        c.execute("INSERT OR IGNORE INTO tweets_by_vasemmisto (id_tweet, content) VALUES (?, ?);", (tweet.id, tweet.text))
        conn.commit()
    print("Requete acceptée pour le parti Vasemmisto")

    for tweet in parti9_tweets:
        unidecode(tweet.text)
        c.execute("INSERT OR IGNORE INTO tweets_by_vihreat (id_tweet, content) VALUES (?, ?);", (tweet.id, tweet.text))
        conn.commit()
    print("Requete acceptée pour le parti Vihreat")

    ###################################

    print("INSERTION DES TWEETS DES LEADERS \n \n")

    for tweet in leader_parti1_tweets:
        unidecode(tweet.text)
        c.execute("INSERT OR IGNORE INTO tweets_by_leader_Demarit (id_tweet, content) VALUES (?, ?);", (tweet.id, tweet.text))
        conn.commit()
    print("Requete acceptée pour le leader du parti Demarit")

    for tweet in leader_parti2_tweets:
        unidecode(tweet.text)
        c.execute("INSERT OR IGNORE INTO tweets_by_leader_Keskusta (id_tweet, content) VALUES (?, ?);", (tweet.id, tweet.text))
        conn.commit()
    print("Requete acceptée pour le leader du parti Keskusta")

    for tweet in leader_parti3_tweets:
        unidecode(tweet.text)
        c.execute("INSERT OR IGNORE INTO tweets_by_leader_Kokoomus (id_tweet, content) VALUES (?, ?);", (tweet.id, tweet.text))
        conn.commit()
    print("Requete acceptée pour le leader du parti Kokoomus")

    for tweet in leader_parti4_tweets:
        unidecode(tweet.text)
        c.execute("INSERT OR IGNORE INTO tweets_by_leader_KDpuolue (id_tweet, content) VALUES (?, ?);", (tweet.id, tweet.text))
        conn.commit()
    print("Requete acceptée pour le leader du parti KDpuolue")

    for tweet in leader_parti5_tweets:
        unidecode(tweet.text)
        c.execute("INSERT OR IGNORE INTO tweets_by_leader_Persut (id_tweet, content) VALUES (?, ?);", (tweet.id, tweet.text))
        conn.commit()
    print("Requete acceptée pour le leader du parti Persut")

    for tweet in leader_parti6_tweets:
        unidecode(tweet.text)
        c.execute("INSERT OR IGNORE INTO tweets_by_leader_SiniTulevaisuus (id_tweet, content) VALUES (?, ?);", (tweet.id, tweet.text))
        conn.commit()
    print("Requete acceptée pour le leader du parti SiniTulevaisuus")

    for tweet in leader_parti7_tweets:
        unidecode(tweet.text)
        c.execute("INSERT OR IGNORE INTO tweets_by_leader_sfprkp (id_tweet, content) VALUES (?, ?);", (tweet.id, tweet.text))
        conn.commit()
    print("Requete acceptée pour le leader du parti sfprkp")

    for tweet in leader_parti8_tweets:
        unidecode(tweet.text)
        c.execute("INSERT OR IGNORE INTO tweets_by_leader_vasemmisto (id_tweet, content) VALUES (?, ?);", (tweet.id, tweet.text))
        conn.commit()
    print("Requete acceptée pour le leader du parti vasemmisto")

    for tweet in leader_parti9_tweets:
        unidecode(tweet.text)
        c.execute("INSERT OR IGNORE INTO tweets_by_leader_vihreat (id_tweet, content) VALUES (?, ?);", (tweet.id, tweet.text))
        conn.commit()
    print("Requete acceptée pour le leader du parti Vihreat")

    for tweet in viceleaders_partiDemarit_tweets:
        unidecode(tweet.text)
        c.execute("INSERT OR IGNORE INTO tweets_viceleaders_Demarit(id, username , content) VALUES (?, ?, ?);", (tweet.id, tweet.author.screen_name, tweet.text))
        conn.commit()
    for tweet in viceleaders_partiKeskusta_tweets:
        unidecode(tweet.text)
        c.execute("INSERT OR IGNORE INTO tweets_viceleaders_Keskusta(id, username , content) VALUES (?, ?, ?);", (tweet.id, tweet.author.screen_name, tweet.text))
        conn.commit()
    for tweet in viceleaders_partiKokoomus_tweets:
        unidecode(tweet.text)
        c.execute("INSERT OR IGNORE INTO tweets_viceleaders_Kokoomus(id, username , content) VALUES (?, ?, ?);", (tweet.id, tweet.author.screen_name, tweet.text))
        conn.commit()
    for tweet in viceleader_parti5_tweets:
        unidecode(tweet.text)
        c.execute("INSERT OR IGNORE INTO tweets_viceleaders_parti5(id, username , content) VALUES (?, ?, ?);", (tweet.id, tweet.author.screen_name, tweet.text))
        conn.commit()
    for tweet in viceleader_parti8_tweets:
        unidecode(tweet.text)
        c.execute("INSERT OR IGNORE INTO tweets_viceleaders_parti8(id, username , content) VALUES (?, ?, ?);", (tweet.id, tweet.author.screen_name, tweet.text))
        conn.commit()

    print("requete acceptée pour les vice présidents et secrétaires connus de chaque parti")

    tweets_parti1 = []
    tweets_parti1.extend(parti1_tweets)
    tweets_parti1.extend(leader_parti1_tweets)
    tweets_parti1.extend(viceleaders_partiDemarit_tweets)

    tweets_parti2 = []
    tweets_parti2.extend(parti2_tweets)
    tweets_parti2.extend(leader_parti2_tweets)
    tweets_parti2.extend(viceleaders_partiKeskusta_tweets)

    tweets_parti3 = []
    tweets_parti3.extend(parti3_tweets)
    tweets_parti3.extend(leader_parti3_tweets)
    tweets_parti3.extend(viceleaders_partiKokoomus_tweets)

    tweets_parti4 = []
    tweets_parti4.extend(parti4_tweets)
    tweets_parti4.extend(leader_parti4_tweets)

    tweets_parti5 = []
    tweets_parti5.extend(parti5_tweets)
    tweets_parti5.extend(leader_parti5_tweets)
    tweets_parti5.extend(viceleader_parti5_tweets)

    tweets_parti6 = []
    tweets_parti6.extend(parti6_tweets)
    tweets_parti6.extend(leader_parti6_tweets)

    tweets_parti7 = []
    tweets_parti7.extend(parti7_tweets)
    tweets_parti7.extend(leader_parti7_tweets)

    tweets_parti8 = []
    tweets_parti8.extend(parti8_tweets)
    tweets_parti8.extend(leader_parti8_tweets)
    tweets_parti8.extend(viceleader_parti8_tweets)

    tweets_parti9 = []
    tweets_parti9.extend(parti9_tweets)
    tweets_parti9.extend(leader_parti9_tweets)

    rep_graph = input("Veuillez sélectionner le parti dont vous voulez analyser les tweets en fonction de la positivité / négativité : \n")

    if rep_graph == '0':
        sentiments_objects = [TextBlob(tweet.text) for tweet in searched_tweets]
        sentiments_values = [[tweet.sentiment.polarity, str(tweet)] for tweet in sentiments_objects]
        fig, ax = plt.subplots(figsize=(8,6))
        sentiments_parti0 = pd.DataFrame(sentiments_values, columns=["polarité", "tweet"])
        sentiments_parti0.hist(bins=[-1, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1], ax = ax, color="blue")
        plt.title("Sentiments sur les tweets des utilisateurs")
        plt.show()

    if rep_graph == '1':
        sentiments_objects = [TextBlob(tweet.text) for tweet in tweets_parti1]
        sentiments_values = [[tweet.sentiment.polarity, str(tweet)] for tweet in sentiments_objects]
        fig, ax = plt.subplots(figsize=(8,6))
        sentiments_parti1 = pd.DataFrame(sentiments_values, columns=["polarité", "tweet"])
        sentiments_parti1.hist(bins=[-1, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1], ax = ax, color="blue")
        plt.title("Sentiments sur les tweets du parti Demarit")
        plt.show()

    
    elif rep_graph == '2':
        sentiments_objects = [TextBlob(tweet.text) for tweet in tweets_parti2]
        sentiments_values = [[tweet.sentiment.polarity, str(tweet)] for tweet in sentiments_objects]
        fig, ax = plt.subplots(figsize=(8,6))
        sentiments_parti2 = pd.DataFrame(sentiments_values, columns=["polarité", "tweet"])
        sentiments_parti2.hist(bins=[-1, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1], ax = ax, color="blue")
        plt.title("Sentiments sur les tweets du parti Keskusta")
        plt.show()

   
    elif rep_graph == '3':
        sentiments_objects = [TextBlob(tweet.text) for tweet in tweets_parti3]
        sentiments_values = [[tweet.sentiment.polarity, str(tweet)] for tweet in sentiments_objects]
        fig, ax = plt.subplots(figsize=(8,6))
        sentiments_parti3 = pd.DataFrame(sentiments_values, columns=["polarité", "tweet"])
        sentiments_parti3.hist(bins=[-1, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1], ax = ax, color="blue")
        plt.title("Sentiments sur les tweets du parti 3")
        plt.show()


    elif rep_graph == '4':
        sentiments_objects = [TextBlob(tweet.text) for tweet in tweets_parti4]
        sentiments_values = [[tweet.sentiment.polarity, str(tweet)] for tweet in sentiments_objects]
        fig, ax = plt.subplots(figsize=(8,6))
        sentiments_parti4 = pd.DataFrame(sentiments_values, columns=["polarité", "tweet"])
        sentiments_parti4.hist(bins=[-1, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1], ax = ax, color="blue")
        plt.title("Sentiments sur les tweets du parti 4")
        plt.show()
        

    elif rep_graph == '5':
        sentiments_objects = [TextBlob(tweet.text) for tweet in tweets_parti5]
        sentiments_values = [[tweet.sentiment.polarity, str(tweet)] for tweet in sentiments_objects]
        fig, ax = plt.subplots(figsize=(8,6))
        sentiments_parti5 = pd.DataFrame(sentiments_values, columns=["polarité", "tweet"])
        sentiments_parti5.hist(bins=[-1, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1], ax = ax, color="blue")
        plt.title("Sentiments sur les tweets du parti 5")
        plt.show()
 

    elif rep_graph == '6':
        sentiments_objects = [TextBlob(tweet.text) for tweet in tweets_parti6]
        sentiments_values = [[tweet.sentiment.polarity, str(tweet)] for tweet in sentiments_objects]
        fig, ax = plt.subplots(figsize=(8,6))
        sentiments_parti6 = pd.DataFrame(sentiments_values, columns=["polarité", "tweet"])
        sentiments_parti6.hist(bins=[-1, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1], ax = ax, color="blue")
        plt.title("Sentiments sur les tweets du parti 6")
        plt.show()
 

    elif rep_graph == '7':
        sentiments_objects = [TextBlob(tweet.text) for tweet in tweets_parti7]
        sentiments_values = [[tweet.sentiment.polarity, str(tweet)] for tweet in sentiments_objects]
        fig, ax = plt.subplots(figsize=(8,6))
        sentiments_parti7 = pd.DataFrame(sentiments_values, columns=["polarité", "tweet"])
        sentiments_parti7.hist(bins=[-1, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1], ax = ax, color="blue")
        plt.title("Sentiments sur les tweets du parti 7")
        plt.show()
 

    elif rep_graph == '8':
        sentiments_objects = [TextBlob(tweet.text) for tweet in tweets_parti8]
        sentiments_values = [[tweet.sentiment.polarity, str(tweet)] for tweet in sentiments_objects]
        fig, ax = plt.subplots(figsize=(8,6))
        sentiments_parti8 = pd.DataFrame(sentiments_values, columns=["polarité", "tweet"])
        sentiments_parti8.hist(bins=[-1, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1], ax = ax, color="blue")
        plt.title("Sentiments sur les tweets du parti 8")
        plt.show()
 
 
    elif rep_graph == '9':
        sentiments_objects = [TextBlob(tweet.text) for tweet in tweets_parti9]
        sentiments_values = [[tweet.sentiment.polarity, str(tweet)] for tweet in sentiments_objects]
        fig, ax = plt.subplots(figsize=(8,6))
        sentiments_parti9 = pd.DataFrame(sentiments_values, columns=["polarité", "tweet"])
        sentiments_parti9.hist(bins=[-1, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1], ax = ax, color="blue")
        plt.title("Sentiments sur les tweets du parti 9")
        plt.show()

    else:
        print("lol")

    # ON UTILISE L'ALGORITHME

    rep = input("Souhaitez vous utiliser LDA ? si oui tapez oui sinon tapez autre chose : \n")

    i = 0

    total_topics = 5
    TEMP_FOLDER = tempfile.gettempdir()
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    
    if rep == 'oui':
        list1 = ['RT', 'rt']
        stoplist = stopwords.words('finnish') + list(punctuation) + list1

        print("application du LDA pour les tweets en rapport avec les élections finlandaises")
    
        texts = [[word for word in str(tweet.text).lower().split() if word not in stoplist] for tweet in searched_tweets]

        dictionary = corpora.Dictionary(texts)
        dictionary.save(os.path.join(TEMP_FOLDER, 'tweets.dict'))

        searched_tweets = [dictionary.doc2bow(text) for text in texts]
        corpora.MmCorpus.serialize(os.path.join(TEMP_FOLDER, 'tweets.mm'), searched_tweets)

        tfidf = models.TfidfModel(searched_tweets)

        searched_tweets_tfidf = tfidf[searched_tweets]

        lda = models.LdaModel(searched_tweets, id2word=dictionary, num_topics=total_topics)
        searched_tweets_lda = lda[searched_tweets_tfidf]

        #panel1 = pyLDAvis.gensim.prepare(lda, searched_tweets, dictionary, sort_topics=True)
        #pyLDAvis.show(panel1)

        ###

        print("application du LDA pour les tweets en rapport avec le parti 1")
        
        texts = [[word for word in str(tweet.text).lower().split() if word not in stoplist] for tweet in tweets_parti1]

        dictionary = corpora.Dictionary(texts)
        dictionary.save(os.path.join(TEMP_FOLDER, 'tweet2.dict'))

        tweets_parti1 = [dictionary.doc2bow(text) for text in texts]
        corpora.MmCorpus.serialize(os.path.join(TEMP_FOLDER, 'tweet2.mm'), tweets_parti1)

        tfidf = models.TfidfModel(tweets_parti1)

        searched_tweets_tfidf = tfidf[tweets_parti1]

        lda = models.LdaModel(tweets_parti1, id2word=dictionary, num_topics=total_topics)
        searched_tweets_lda = lda[searched_tweets_tfidf]

        ###

        print("application du LDA pour les tweets en rapport avec le parti 2")
        
        texts = [[word for word in str(tweet.text).lower().split() if word not in stoplist] for tweet in tweets_parti2]

        dictionary = corpora.Dictionary(texts)
        dictionary.save(os.path.join(TEMP_FOLDER, 'tweet3.dict'))

        tweets_parti2 = [dictionary.doc2bow(text) for text in texts]
        corpora.MmCorpus.serialize(os.path.join(TEMP_FOLDER, 'tweet3.mm'), tweets_parti2)

        tfidf = models.TfidfModel(tweets_parti2)

        searched_tweets_tfidf = tfidf[tweets_parti2]

        lda = models.LdaModel(tweets_parti2, id2word=dictionary, num_topics=total_topics)
        searched_tweets_lda = lda[searched_tweets_tfidf]

       
        ###

        print("application du LDA pour les tweets en rapport avec le parti 3")
        
        texts = [[word for word in str(tweet.text).lower().split() if word not in stoplist] for tweet in tweets_parti3]

        dictionary = corpora.Dictionary(texts)
        dictionary.save(os.path.join(TEMP_FOLDER, 'tweet4.dict'))

        tweets_parti3 = [dictionary.doc2bow(text) for text in texts]
        corpora.MmCorpus.serialize(os.path.join(TEMP_FOLDER, 'tweet4.mm'), tweets_parti3)

        tfidf = models.TfidfModel(tweets_parti3)

        searched_tweets_tfidf = tfidf[tweets_parti3]

        lda = models.LdaModel(tweets_parti3, id2word=dictionary, num_topics=total_topics)
        searched_tweets_lda = lda[searched_tweets_tfidf]

        print("application du LDA pour les tweets en rapport avec le parti 4")
        
        texts = [[word for word in str(tweet.text).lower().split() if word not in stoplist] for tweet in tweets_parti4]

        dictionary = corpora.Dictionary(texts)
        dictionary.save(os.path.join(TEMP_FOLDER, 'tweet5.dict'))

        tweets_parti4 = [dictionary.doc2bow(text) for text in texts]
        corpora.MmCorpus.serialize(os.path.join(TEMP_FOLDER, 'tweet5.mm'), tweets_parti4)

        tfidf = models.TfidfModel(tweets_parti4)

        searched_tweets_tfidf = tfidf[tweets_parti4]

        lda = models.LdaModel(tweets_parti4, id2word=dictionary, num_topics=total_topics)
        searched_tweets_lda = lda[searched_tweets_tfidf]

        lda.show_topics(total_topics, 5)

        ##

        print("application du LDA pour les tweets en rapport avec le parti 5")
        
        texts = [[word for word in str(tweet.text).lower().split() if word not in stoplist] for tweet in tweets_parti5]

        dictionary = corpora.Dictionary(texts)
        dictionary.save(os.path.join(TEMP_FOLDER, 'tweet6.dict'))

        tweets_parti5 = [dictionary.doc2bow(text) for text in texts]
        corpora.MmCorpus.serialize(os.path.join(TEMP_FOLDER, 'tweet6.mm'), tweets_parti5)

        tfidf = models.TfidfModel(tweets_parti5)

        searched_tweets_tfidf = tfidf[tweets_parti5]

        lda = models.LdaModel(tweets_parti5, id2word=dictionary, num_topics=total_topics)
        searched_tweets_lda = lda[searched_tweets_tfidf]

        lda.show_topics(total_topics, 5)

        ###

        print("application du LDA pour les tweets en rapport avec le parti 6")
        
        texts = [[word for word in str(tweet.text).lower().split() if word not in stoplist] for tweet in tweets_parti6]

        dictionary = corpora.Dictionary(texts)
        dictionary.save(os.path.join(TEMP_FOLDER, 'tweet7.dict'))

        tweets_parti6 = [dictionary.doc2bow(text) for text in texts]
        corpora.MmCorpus.serialize(os.path.join(TEMP_FOLDER, 'tweet7.mm'), tweets_parti6)

        tfidf = models.TfidfModel(tweets_parti6)

        searched_tweets_tfidf = tfidf[tweets_parti6]

        lda = models.LdaModel(tweets_parti6, id2word=dictionary, num_topics=total_topics)
        searched_tweets_lda = lda[searched_tweets_tfidf]

        lda.show_topics(total_topics, 5)

        ###

        print("application du LDA pour les tweets en rapport avec le parti 7")
        
        texts = [[word for word in str(tweet.text).lower().split() if word not in stoplist] for tweet in tweets_parti7]

        dictionary = corpora.Dictionary(texts)
        dictionary.save(os.path.join(TEMP_FOLDER, 'tweet8.dict'))

        tweets_parti7 = [dictionary.doc2bow(text) for text in texts]
        corpora.MmCorpus.serialize(os.path.join(TEMP_FOLDER, 'tweet8.mm'), tweets_parti7)

        tfidf = models.TfidfModel(tweets_parti7)

        searched_tweets_tfidf = tfidf[tweets_parti7]

        lda = models.LdaModel(tweets_parti7, id2word=dictionary, num_topics=total_topics)
        searched_tweets_lda = lda[searched_tweets_tfidf]

        lda.show_topics(total_topics, 5)

        ###

        print("application du LDA pour les tweets en rapport avec le parti 8")
        
        texts = [[word for word in str(tweet.text).lower().split() if word not in stoplist] for tweet in tweets_parti8]

        dictionary = corpora.Dictionary(texts)
        dictionary.save(os.path.join(TEMP_FOLDER, 'tweet9.dict'))

        tweets_parti8 = [dictionary.doc2bow(text) for text in texts]
        corpora.MmCorpus.serialize(os.path.join(TEMP_FOLDER, 'tweet9.mm'), tweets_parti8)

        tfidf = models.TfidfModel(tweets_parti8)

        searched_tweets_tfidf = tfidf[tweets_parti8]

        lda = models.LdaModel(tweets_parti8, id2word=dictionary, num_topics=total_topics)
        searched_tweets_lda = lda[searched_tweets_tfidf]

        lda.show_topics(total_topics, 5)

        ###

        print("application du LDA pour les tweets en rapport avec le parti 9")
        
        texts = [[word for word in str(tweet.text).lower().split() if word not in stoplist] for tweet in tweets_parti9]

        dictionary = corpora.Dictionary(texts)
        dictionary.save(os.path.join(TEMP_FOLDER, 'tweet99.dict'))

        tweets_parti9 = [dictionary.doc2bow(text) for text in texts]
        corpora.MmCorpus.serialize(os.path.join(TEMP_FOLDER, 'tweet99.mm'), tweets_parti9)

        tfidf = models.TfidfModel(tweets_parti9)

        searched_tweets_tfidf = tfidf[tweets_parti9]

        lda = models.LdaModel(tweets_parti9, id2word=dictionary, num_topics=total_topics)
        searched_tweets_lda = lda[searched_tweets_tfidf]

        panel9 = pyLDAvis.gensim.prepare(lda, tweets_parti9, dictionary, sort_topics=True)
        pyLDAvis.show(panel9)

if __name__ == "__main__":
    main()
