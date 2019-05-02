from nltk.tokenize import *
from nltk.corpus import *

data = "Salut tout le monde c'est diablox9"
stopWords = set(stopwords.words('english'))

phrases = sent_tokenize(data)
words = word_tokenize(data)
wordsfiltered = []


for w in words:
    if w not in stopWords:
        wordsfiltered.append(w)

print(wordsfiltered)
print(len(stopWords))
