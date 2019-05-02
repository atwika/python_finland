from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

words = ["habitant","habitation","habite","habiter"]
ps = PorterStemmer()

for word in words:
    print(ps.stem(word))
    
