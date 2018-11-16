
# coding: utf-8

# # List of companies that sponsor H1B's.

# Step 1: Scraping the data from redbus2us.com and storing it in the data frame. <br>
# Step 2: Using pandas to clean the data and finally visualize the data using various libraries. <br>
# Step 3: The cleaned data will then be saved in .csv file format.

# Refereces: <br>
# https://towardsdatascience.com/an-introduction-to-web-scraping-with-python-bc9563fe8860 <br>
# https://www.datacamp.com/community/tutorials/web-scraping-using-python <br>
# https://dev.to/tomoyukiaota/visualizing-the-patterns-of-missing-value-occurrence-with-python-46dj

# In[1]:

# importing libraries
import re
import pandas as pd
from bs4 import BeautifulSoup
import requests 
import csv
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic('matplotlib inline')


# In[2]:

# Get the html contents from the page. This is done using the requests library
page="http://redbus2us.com/h1b-visa-sponsors/?searchText=&searchCity=new-york&searchYear=16&action=search&searchJobTitle="
r = requests.get(page)
c = r.content


# In[3]:

#Parse the html. This is done with BeautifulSoup.
soup = BeautifulSoup(c,"html.parser")
type(soup)


# In[4]:

title=soup.title
print(title)


# In[5]:

rows = soup.find_all('tr')
print(rows[:5])


# # Data Manipulation & Cleaning

# In[6]:

str_cells = str(rows)
cleantext = BeautifulSoup(str_cells, "lxml").get_text()
print(cleantext)


# In[7]:

list_rows = []
for row in rows:
    cells = row.find_all('td')
    str_cells = str(cells)
    clean = re.compile('<.*?>')
    clean2 = (re.sub(clean, '',str_cells))
    list_rows.append(clean2)
print(clean2)
#type(clean2)


# In[8]:

df = pd.DataFrame(list_rows)
df.head(10)


# In[9]:

#Spliting rows 
df1 = df[0].str.split(',', expand=True)
df1.head(10)


# In[10]:

# removing the '[]' from the rows
df1[0] = df1[0].str.strip('[')
df1[4] = df1[4].str.strip(']')
df1.head(10)


# In[11]:

# 1st row to be header
df2 = df1.rename(columns=df1.iloc[0])
df2.head(10)


# In[12]:

#Dropping Index row
#df3 = df2.drop(df2.index[0])
df3=df2.drop([0],axis=0)
df3.head(10)


# In[13]:

# Changing na to 0
df4 = df3.fillna(0)
df4.head()


# In[14]:

#At this point, the table is almost properly formatted.
#For analysis, you can start by getting an overview of the data as shown below.
df4.info()
df4.shape


# # Storing the data in Csv file format
# 

# In[34]:

# To write the dataframe to a csv file
df4.to_csv("H1b sponsoring companies in 2016.csv")


# # Data Analysis & Visualization

# In[15]:

df4.describe()


# In[16]:

#sns.heatmap(df4.isnull(), cbar=False)


# In[17]:

# Another method to find missing value is : <br> 
# pip install missingno
import missingno as msno


# In[18]:

msno.matrix(df4)


# This indicates no missing values.

# In[33]:

#another method 
#msno.heatmap(df1)


# In[ ]:



