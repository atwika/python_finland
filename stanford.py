import os
java_path = "C:/Program Files (x86)/Java/jre1.8.0_211/bin/java.exe"
os.environ['JAVAHOME'] = java_path

import nltk

nltk.internals.config_java("C:/Program Files (x86)/Java/jre1.8.0_211/bin/java.exe")

from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

st = StanfordNERTagger('stanford/classifiers/english.all.3class.distsim.crf.ser.gz','stanford/stanford-ner.jar',encoding='utf-8')
text = input('Entrer la phrase que vous voulez, si possible composé de prenoms, verbes, pays etc \n')
tokenized_text = word_tokenize(text) # On divise la phrase morceau par morceau, en tokens
classified_text = st.tag(tokenized_text)

print(classified_text)
