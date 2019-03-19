
# coding: utf-8

# ## Web Scraping
# > webbrowser Comes with Python and opens a browser to a specific page.<br>
# Requests Downloads files and web pages from the Internet. <br>
# Beautiful Soup Parses HTML, the format that web pages are written in.<br>
# Selenium Launches and controls a web browser. Selenium is able to fill in forms and simulate mouse clicks in this browser.

# In[ ]:

import webbrowser


# In[ ]:

# Opens the given URL
webbrowser.open('https://en.wikipedia.org/wiki/Web_scraping')


# ### Downloading a web page with Request.get() function

# In[ ]:

import requests
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')


# In[ ]:

type(res)


# In[ ]:

res.status_code == requests.codes.ok


# In[ ]:

print(res.text[:296])


# ### Check for errors

# In[ ]:

import requests
res = requests.get('https://marvelapp.com/asdf')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))


# In[ ]:



