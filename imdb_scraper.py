import requests
from bs4 import BeautifulSoup as bsoup
import pandas as pd
import numpy as np

# url of imbd top 1000 movies
URL = "https://www.imdb.com/search/title/?groups=top_1000&ref_=adv_prv"
headers = {"Accept-Language": "en-US, en;q=0.5"}
results = requests.get(URL, headers=headers)

soup = bsoup(results.text, "html.parser")

# data of each movie
titles = []
years = []
time = []
imdb_ratings = []
metascores = []
votes = []
gross = []

# find all divs containing data for each movie
movie_divs = soup.find_all('div', class_='lister-item mode-advanced')