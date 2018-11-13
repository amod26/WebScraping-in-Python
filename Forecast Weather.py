
# coding: utf-8

# In[2]:

# Import libraries

import requests #used to query website

from bs4 import BeautifulSoup

# to parse and render data from the website

import pandas as pd


# In[3]:

# specify the url
page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")

print(page.text)

#Parse the html in the page variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page.content, 'html.parser')


# In[4]:

# here main part is whole weeks forecasting data which comes under tombstone-container class in webpage individually
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")

tonight = forecast_items[0]
print(tonight.prettify())



# In[5]:

#extract important information from tonight
period = tonight.find(class_="period-name").get_text()
print(period)

short_desc = tonight.find(class_="short-desc").get_text()
print(short_desc)

temp = tonight.find(class_="temp").get_text()
print(temp)


# In[6]:

#To extraxct information from the image tag ot tonight variable
img = tonight.find("img")
desc = img['title']

print(desc)


# In[7]:

#Extracr the information from whole webpage
period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
print("\n \n",periods)


# In[8]:

# Extract the above three information short_desc, temp and title information for all days of week
short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
print(short_descs)

temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
print(temps)

descs = [d["title"] for d in seven_day.select(".tombstone-container img")]
print(descs)


# In[9]:

#Combine this data into pandas data frame:-
weather = pd.DataFrame({
    "period": periods,
    "short_desc": short_descs,
    "temp": temps,
    "desc": descs
})

print("\n \n")
print("Wheather Deatils of particular week \n",weather)



# In[10]:

# to save the pandas datafrmame data into the excel :-
writer = pd.ExcelWriter('Weather1.xls')
weather.to_excel(writer,'Sheet1')
writer.save()



# In[ ]:



