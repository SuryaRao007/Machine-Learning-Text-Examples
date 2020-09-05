# -*- coding: utf-8 -*-
"""
Created on Wed May 20 09:53:00 2020

@author: Surya
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


""""Part of speech tagging"""
nltk.download('averaged_perceptron_tagger')
nltk.download('tagsets')
import nltk

text = """I collected the weights of a flock of geese,
 then calculated the mean. What is the meaning of this? As a goose!"""
text_word = nltk.tokenize.word_tokenize(text)
nltk.pos_tag(text_word)
nltk.help.upenn_tagset('JJ')
