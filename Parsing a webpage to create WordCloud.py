
# coding: utf-8

# In[44]:

import bs4
from bs4 import BeautifulSoup
from lxml import html # Library for parsing XML & HTML
import requests
from wordcloud import WordCloud
import matplotlib.pyplot as plt 


# In[45]:

# retrieve the web page with requests.get method and store it in page
page = requests.get('http://changingminds.org/disciplines/job-finding/resume/resume_power_words.htm') 


# In[46]:

type(page) # contains entire webpage, hence we change it to soup


# In[47]:

page = bs4.BeautifulSoup(page.text,'lxml')


# In[48]:

type(page)


# In[49]:

hi= page.select('title') # selecting title
hi


# In[53]:

hi[0] # selecting using indexing


# In[58]:

words=page.select('.quote') # selecting target class 
words


# In[89]:

for i in page.select('.quote'): 
    print(i.text)     # printing only text 


# In[73]:

i.text


# In[97]:

cloud = WordCloud(background_color="white",max_words=300).generate(i.text)


# In[98]:

plt.figure( figsize=(10,8) )
plt.imshow(cloud)
plt.title('Power Words for Resume')
plt.axis('off')
plt.show()


# In[ ]:



