# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
import pandas as pd
import os
print ('my working directory:\n' + os.getcwd())
from nltk.tokenize import RegexpTokenizer
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
nltk.download('stopwords')
from nltk.corpus import stopwords
nltk.download('inaugural')
from nltk.corpus import inaugural

text = """I collected the weights of a flock of geese,
 then calculated the mean. What is the maning of this? As a goose!"""
t1 = nltk.tokenize.word_tokenize(text)
t2_words = [w.lower() for w in t1 if w not in ('.','?','!',',') and w not in 
            stopwords.words('english')]
t2_words
porter = nltk.PorterStemmer()
lancaster = nltk.LancasterStemmer()
snowball = nltk.SnowballStemmer('english')
df1 = pd.DataFrame({'raw_word':t2_words})
df1['porter'] = [porter.stem(t) for t in t2_words]
df1['lancaster']=[lancaster.stem(t) for t in t2_words]
df1['snowball']=[snowball.stem(t) for t in t2_words]
df1['porter']
df1
""""Lemmatizer"""
nltk.download('wordnet')
wnl = nltk.WordNetLemmatizer()
df1['lemma']= [wnl.lemmatize(t) for t in t2_words]
df1

""""Part of speech tagging"""

