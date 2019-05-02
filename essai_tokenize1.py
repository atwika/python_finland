import nltk
from nltk.tokenize import *

document = "Bonjour et bienvenue sur NLTK"

mots = nltk.sent_tokenize(document)

for mot in mots:
    print(nltk.pos_tag(nltk.word_tokenize(mot)))
