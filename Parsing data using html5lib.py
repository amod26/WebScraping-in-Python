
# coding: utf-8

# In[3]:

import pandas as pd


# In[4]:

# you need to install html5lib
# pip install html5lib
# reading data from a html site
df = pd.read_html('https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations')


# In[5]:

# get part that has the states and abbreviations
df_usa = df[0]


# In[6]:

# remove unnecessary rows and columns
final_df = df_usa.drop(df_usa.index[range(0,11)]).drop(df_usa.columns[range(10,15)], axis=1)


# In[7]:

# rename columns
final_df.rename(columns={0: 'Region Name', 1: 'Region Status', 2: 'ISO', 3: 'ANSI_Letter', 4: 'ANSI_Code'
                         , 5: 'USPS', 6: 'USCG', 7: 'GPO', 8: 'AP', 9: 'Other Abbreviations'}, inplace=True)


# In[8]:

# reset index of rows
final_df.reset_index(drop=True)


# In[ ]:



