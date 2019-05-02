import nltk
from nltk.book import *
import matplotlib
import numpy
from nltk.corpus import brown
from nltk.corpus import wordnet as wn

def diversite_lex(text):

    
    print("Voici le nombre de mots entiers du texte : " + str(len(text)))
    print("Voici la taille du vocabulaire : " + str(len(set(text))))

    div_lex = len(text) / len(set(text))
    print("calcul de la diversité lexicale : " + str(div_lex))


def trouver_mot(mot, text):
    print("Le mot " + mot + " apparait " + str(text.count(mot)) + " fois dans le texte choisi")
    
    
def imprimer_courbe(text):
    fdist2 = FreqDist(text)
    fdist2.plot(50, cumulative = True)
    
def iteration_fct(text):

    fdist2 = FreqDist(text)

    longueur = input("saisissez la longueur minimum en caractères : ")

    nb_iteration = input("saisissez le nombre minimum d'iterations : ")
    
    print(sorted([w for w in set(text) if len(w) > int(longueur) and fdist2[w] > int(nb_iteration)]))


def freq_mots(text):

    fdist22 = FreqDist([len(w) for w in text])
    print(fdist22.keys())

    print(fdist22.items())
    
def compt_ends(text):

    endword = input("entrer la fin : ")

    print(sorted([w for w in set(text) if w.endswith(endword)]))

def diffdocs(*modaux):
    news_text = brown.words(categories = 'news')
    fdist = nltk.FreqDist([w.lower() for w in news_text])
    for m in modaux:
        print(m + " : " + str(fdist[m]))

def unusual_words(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    unusual = text_vocab.difference(english_vocab)
    print(sorted(unusual))

def trouver_sens(word):
    print(wn.synsets(word))

def trouver_syn(word):
    print(wn.synset(word).lemma_names)

def definition_mot(word):
    print(wn.synset(word).definition)

def semantic_distancies():

    i = 1
    print("veuillez entrer 5 animals a la suite :")
    first = input("premier mot : ")
    second = input("second mot : ")
    third = input("troisieme mot : ")
    fourth = input("quatrieme mot : ")
    five = input("cinquieme mot : ")

    first = wn.synset(first)
    second = wn.synset(second)
    third = wn.synset(third)
    fourth = wn.synset(fourth)
    five = wn.synset(five)
    
    print(first.lowest_common_hypernyms(second))
    print(first.lowest_common_hypernyms(third))
    print(first.lowest_common_hypernyms(fourth))
    print(first.lowest_common_hypernyms(five))

    print("//////////////////////////////////////////")

    print(first.path_similarity(second))
    print(first.path_similarity(third))
    print(first.path_similarity(fourth))
    print(first.path_similarity(five))


def lemmatisation():
    phrase = input("Entrez une phrase : ")
    tokens = nltk.word_tokenize(phrase)
    wnl = nltk.WordNetLemmatizer()
    rep = [wnl.lemmatize(t) for t in tokens]
    print(rep)

def identify_tag():
    phrase = input("Entrez une phrase : ")
    tokens = nltk.word_tokenize(phrase)
    print(nltk.pos_tag(tokens))
