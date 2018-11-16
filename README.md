# WebScraping-in-Python
Web scraping is an automatic process of extracting information from web. Web scraping is also called as web data mining or web harvesting, is the process of constructing an agent which can extract, parse, download and organize useful information from the web automatically. 

PS: Before we scrape a website, we need to take a look at their robots.txt. This file tells us if the website allows scraping or if they do not. To find the robots.txt, type in the base url and add “/robots.txt”. For eg, if we want to crawl www.h1bdata.info type in https://h1bdata.info/robots.txt at the url box.

If the robots.txt allows full access it says as follows:

User-agent: *

Disallow:

If the robots.txt blocks all access, it contains the following:

User-agent: *

Disallow: /

********************************************************************************************************

Step 1: Downloading Contents from Web Pages 

In this step, a web scraper will download the requested contents from multiple web pages.

Step 2: Extracting Data

The data on websites is HTML and mostly unstructured. Hence, in this step, web scraper will parse and extract structured data from the downloaded contents.

Step 3: Storing the Data

Here, a web scraper will store and save the extracted data in any of the format like CSV, JSON or in database.

Step 4: Analyzing the Data

After all these steps are successfully done, the web scraper will analyze the data thus obtained.

********************************************************************************************************

 Below are the contents of the files in this repository.
1. News Article Summary
- Parses news article and summarizes the content and saves it in a CSV file.

2. Generating Word Cloud using beautifulsoup library.
- Webscraped a webpage leveraging the beautifulsoup library in python. Scraped all the power words required in a resume and visualized it using the Wordcloud library in png file format.

3. Weather Forecast.
- Webscraped a weather forecast webpage using beautifulsoup library, extracted the required data and stored it in pandas dataframe. Stored the final output in excel file.

4. H1B sponsoring companies in 2016
- Webscraped the data from a website database of H1B sponsoring companies. Cleaned the data, visualized using various libraries, performed various analysis.
