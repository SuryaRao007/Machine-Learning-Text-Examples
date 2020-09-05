# -*- coding: utf-8 -*-
"""
Created on Thu May 21 19:26:33 2020

@author: jyoth
"""

from nltk.tokenize import word_tokenize
import pandas as pd

text1 = 'The computer computer computer science age has been here. Here it is!'
text2 = 'The machine learning age has arrived! Machine learning is fun.'
wlist1 = [w.lower() for w in word_tokenize(text1) if w not in ('.',',','!')]
wlist2 = [w.lower() for w in word_tokenize(text2) if w not in ('.',',','!')]
wlist1
wlist2
fd1 = nltk.FreqDist(wlist1)
fd1
fd1.most_common(3)
fd2 = nltk.FreqDist(wlist2)
fd2
df1 = pd.DataFrame([fd1, fd2])
df1['docid']=[1,2]
df1
df2 = df1.fillna(0)
df2
from scipy import sparse
import numpy as np
td_csr = sparse.csr_matrix(df2)
td_csc = sparse.csr_matrix(df2)
td_dens = np.array(df2)
td_dens.nbytes
td_csr.data.nbytes
td_csc.data.nbytes
""""Matrix standardization, we are concerned withe relative occurence of a term in a document 
a term probability matrix, obtained by dividing the frequencies by total row sum"""
df2.div(df2.sum(axis=1), axis=0)
df2.sum(axis=1)
print(1/13)
