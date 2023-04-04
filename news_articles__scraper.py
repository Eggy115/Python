# -*- coding: utf-8 -*-
"""News_Articles__Scraper.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1v1XaNvdBmHIG79KQyaVUl793rKsV7qTD

***Uncomment the line to install newspaper3k first***
"""

# ! pip install newspaper3k

import pickle
import re
import sys
import urllib

import pandas as pd
import requests

# importing necessary libraries
from bs4 import BeautifulSoup
from newspaper import Article

# Extracting links for all the pages (1 to 158) of boomlive fake news section
fakearticle_links = []
for i in range(1, 159):
    url = "https://www.boomlive.in/fake-news/" + str(i)
    try:
        # this might throw an exception if something goes wrong.
        page = requests.get(url)

        # send requests
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")

        # Collecting all the links in a list
        for content in soup.find_all("h2", attrs={"class": "entry-title"}):
            link = content.find("a")
            fakearticle_links.append(link.get("href"))

    # this describes what to do if an exception is thrown
    except Exception as e:
        # get the exception information
        error_type, error_obj, error_info = sys.exc_info()
        # print the link that cause the problem
        print("ERROR FOR LINK:", url)
        # print error info and line that threw the exception
        print(error_type, "Line:", error_info.tb_lineno)
        continue

fakearticle_links[:5]

len(fakearticle_links)

fakearticle_links[1888:]

import matplotlib.pyplot as plt
import pandas as pd

import numpy as np

"""We have to modify the links so that the links actually work as we can see that the string extracted is the last part of the url!

**We have to add 'https://www.boomlive.in/fake-news' to the extracted links.**
"""

# Modify the links so that it takes us to the particular website
str1 = "https://www.boomlive.in/fake-news"
fakearticle_links = [str1 + lnk for lnk in fakearticle_links]

fakearticle_links[6:10]

"""**The links are modified and is working :)**

***Creating a dataset of all the fake articles***
"""

# Create a dataset for storing the news articles
news_dataset = pd.DataFrame(fakearticle_links, columns=["URL"])

news_dataset.head()

title, text, summary, keywords, published_on, author = (
    [],
    [],
    [],
    [],
    [],
    [],
)  # Creating empty lists to store the data
for Url in fakearticle_links:
    article = Article(Url)

    # Call the download and parse methods to download information
    try:
        article.download()
        article.parse()
        article.nlp()
    except Exception as error:
        print(f"exception : {error}")
        pass

    # Scrape the contents of article
    title.append(article.title)  # extracts the title of the article
    text.append(article.text)  # extracts the whole text of article
    summary.append(article.summary)  # gives us a summary abou the article
    keywords.append(", ".join(article.keywords))  # the main keywords used in it
    published_on.append(article.publish_date)  # the date on which it was published
    author.append(article.authors)  # the authors of the article

"""**Checking the lists created**"""

text[6]

keywords[1]

published_on[6]

author[6]

# Adding the columns in the fake news dataset
news_dataset["title"] = title
news_dataset["text"] = text
news_dataset["keywords"] = keywords
news_dataset["published date"] = published_on
news_dataset["author"] = author

# Check the first five columns of dataset created
news_dataset.head()

"""**Converting the dataset to a csv file**"""

news_dataset.to_csv("Fake_news.csv")

"""**Reading the csv file**"""

df = pd.read_csv("Fake_news.csv")

# Checking the last 5 rows of the csv file
df.tail(5)

"""**Download the csv file in local machine**"""

from google.colab import files

files.download("Fake_news.csv")

"""**Scraping news from Times of India**"""

TOIarticle_links = (
    []
)  # Creating an empty list of all the urls of news from Times of India site

# Extracting links for all the pages (2 to 125) of boomlive fake news section
for i in range(2, 126):
    url = "https://timesofindia.indiatimes.com/news/" + str(i)

    try:
        # send requests
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")

        # Collecting all the links in a list
        for content in soup.find_all("span", attrs={"class": "w_tle"}):
            link = content.find("a")
            TOIarticle_links.append(link.get("href"))

    # this describes what to do if an exception is thrown
    except Exception as e:
        # get the exception information
        error_type, error_obj, error_info = sys.exc_info()
        # print the link that cause the problem
        print("ERROR FOR LINK:", url)
        # print error info and line that threw the exception
        print(error_type, "Line:", error_info.tb_lineno)
        continue

TOIarticle_links[6:15]

len(TOIarticle_links)

str2 = "https://timesofindia.indiatimes.com"
TOIarticle_links = [str2 + lnk for lnk in TOIarticle_links if lnk[0] == "/"]

TOIarticle_links[5:8]

len(TOIarticle_links)

title, text, summary, keywords, published_on, author = (
    [],
    [],
    [],
    [],
    [],
    [],
)  # Creating empty lists to store the data
for Url in TOIarticle_links:
    article = Article(Url)

    # Call the download and parse methods to download information
    try:
        article.download()
        article.parse()
        article.nlp()
    except Exception:
        pass

    # Scrape the contents of article
    title.append(article.title)  # extracts the title of the article
    text.append(article.text)  # extracts the whole text of article
    summary.append(article.summary)  # gives us a summary abou the article
    keywords.append(", ".join(article.keywords))  # the main keywords used in it
    published_on.append(article.publish_date)  # the date on which it was published
    author.append(article.authors)  # the authors of the article

title[5]

TOI_dataset = pd.DataFrame(TOIarticle_links, columns=["URL"])
# Adding the columns in the TOI news dataset
TOI_dataset["title"] = title
TOI_dataset["text"] = text
TOI_dataset["keywords"] = keywords
TOI_dataset["published date"] = published_on
TOI_dataset["author"] = author

TOI_dataset.head()

TOI_dataset.to_csv("TOI_news_dataset.csv")

dt = pd.read_csv("TOI_news_dataset.csv")

dt.tail(3)

from google.colab import files

files.download("TOI_news_dataset.csv")
