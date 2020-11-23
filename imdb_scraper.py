import requests
from bs4 import BeautifulSoup as bsoup
import pandas
import numpy as np

# url of imbd top 1000 movies
URL = "https://www.imdb.com/search/title/?groups=top_1000&ref_=adv_prv"
headers = {"Accept-Language": "en-US, en;q=0.5"}
results = requests.get(URL, headers=headers)

soup = bsoup(results.text, "html.parser")

# data of each movie
titles = []
years = []
runtimes = []
ratings = []
metascores = []
votes = []
grosses = []

# find all divs containing data for each movie
movie_divs = soup.find_all('div', class_='lister-item mode-advanced')

for div in movie_divs:
    name = div.h3.a.text
    titles.append(name)

    year = div.h3.find('span', class_='lister-item-year').text
    years.append(year)

    runtime = div.p.find('span', class_='runtime').text
    runtimes.append(runtime)

    rating = float(div.strong.text)
    ratings.append(rating)

    score = div.find('span', class_='metascore').text if div.find('span', class_='metascore') else '-'
    metascores.append(score)

    # nv contains the class for both the votes and gross (if it is present) <span> tags
    nv = div.find_all('span', attrs={'name': 'nv'})

    vote = nv[0].text
    votes.append(vote)

    gross = nv[1].text if len(nv) > 1 else '-'
    grosses.append(gross)

movies = pandas.DataFrame({
    'movie': titles,
    'year': years,
    'runtime': runtime,
    'imdb': ratings,
    'metascore': metascores,
    'votes': votes,
    'grossMillions': gross,
})

# CLEANING DATA

# remove brackets from year and cast string to int
movies['year'] = movies['year'].str.extract('(\d+)').astype(int)

# remove ' min' from runtime and cast string to int
movies['runtime'] = movies['runtime'].str.extract('(\d+)').astype(int)

# convert grossMillions to numeric (int) and transform dashes into NaN values
movies['metascore'] = pandas.to_numeric(movies['metascore'], errors='coerce')

# remove commas from votes and cast string to int
movies['votes'] = movies['votes'].str.replace(',', '').astype(int)

# remove '$' and 'M' from grossMillions and cast string to int
movies['grossMillions'] = movies['grossMillions'].map(lambda x: x.lstrip('$').rstrip('M'))

# convert grossMillions to numeric (float) and transform dashes into NaN values
movies['grossMillions'] = pandas.to_numeric(movies['grossMillions'], errors='coerce')