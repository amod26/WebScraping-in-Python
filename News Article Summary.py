
# coding: utf-8

# # Create a summary of a news article

# Before we start we need to install following packages: <br>
# 1.pip3 install newspaper3k <br>
# 2.pip install -U textblob <br>
# 3.pip install requests <br>
# 4.sudo pip install -U nltk <br>
# 5.python -m textblob.download_corpora <br>
# 6.nltk.download('punkt')
# 

# In[5]:

import numpy as np
import pandas as pd
import pip
import newspaper
from newspaper import Article
from  textblob import TextBlob
import nltk

from nltk import word_tokenize,sent_tokenize


# In[6]:

url = 'https://www.nytimes.com/2018/11/12/obituaries/stan-lee-dead.html'
article = newspaper.Article(url)
article.download()
article.parse()
article.title
article.nlp()
article.keywords
article.summary
blob2 = TextBlob(article.text)


# In[7]:

wordlist = pd.DataFrame()
ssList=[]
for t in blob2.sentences:
    ww = []
    for word, tag in t.tags:
        if tag in ('NN', 'NNS', 'NNP', 'NNPS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'):
            ww.append(word.lemmatize())
    ss = ' '.join(ww)
    ssList.append(ss.lower())


# In[8]:

wordlist = wordlist.append(ssList, ignore_index=True)    

wordlist
len(blob2.sentences)
wordlist.to_csv('StanLeeSummary.csv')

