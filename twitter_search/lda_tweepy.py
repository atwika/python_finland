import tweepy
import csv
import pandas


# FONCTIONS INTERNET

def lemmatize_stemming(text):
    return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))
def preprocess(text):
    result = []
    for token in gensim.utils.simple_preprocess(text):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            result.append(lemmatize_stemming(token))
    return result

### ON RECUPERE LES TWEETS ET LES ENREGISTRE DANS UN CSV

auth = tweepy.OAuthHandler("NLZ39ilLBflHHt8myenHdH3Ao", "FJ5EAa7DMtnrUHPFNXMuG0heucpzZPatYJNjoixFniWMK8WM0o")

auth.set_access_token("1117700066255474688-5BSckADfdnZTX1WAgTBQib1tnEXBMO", "eiTGX94V9NRpXr9cI5j29oR59MzVp1NeVhHNKCrl4xEWl")

api = tweepy.API(auth)

all_tweets = []

search_word = input("sujet ? \n")


for pages tweepy.Cursor(api.search, q = search_word, lang = "en", since = "2019-04-01").items(200)

out_tweets = [[tweet.text.encode("utf-8")] for tweet in all_tweets]

with open('%s_tweets.csv' % search_word, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["text"])
    writer.writerows(out_tweets)

pass

### ON OUVRE LE CSV POUR TOKENIZE LES TWEETS

data = pandas.read_csv('%s_tweets.csv' % search_word, error_bad_lines=False)
data_text = data[['text']]
data_text['index'] = data_text.index
documents = data_text
print(documents)
print("\n \n \n \n")


nb = input("selection de l'id du tweet : ")



doc_sample = documents[documents["index"] == nb].values
words = []
for word in doc_sample.split(' '):
    words.append(word)
print(words)
print("\n \n on tokenize et lemmatize le document : \n")
print(preprocess(doc_sample))

