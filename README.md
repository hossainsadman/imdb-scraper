# IMDB Top 1000 Movies
This project scrapes the [IMDb "Top 1000" movies (sorted by popularity)](https://www.imdb.com/search/title/?groups=top_1000) webpages and outputs the data to a CSV file.

## Sample Output

|    | movie                      | year | runtime | imdb | metascore | votes   | grossMillions |
| -- | -------------------------- | ---- | ------- | ---- | --------- | ------- | ------------- |
| 0  | Dara of Jasenovac          | 2020 | 130     | 8.7  |           | 51892   |               |
| 1  | Soul                       | 2020 | 100     | 8.1  | 83.0      | 172275  |               |
| 2  | Groundhog Day              | 1993 | 101     | 8.0  | 72.0      | 580305  | 70.91         |
| 3  | The Sound of Music         | 1965 | 172     | 8.0  | 63.0      | 206581  | 163.21        |
| 4  | Avengers: Endgame          | 2019 | 181     | 8.4  | 78.0      | 815967  | 858.37        |
| 5  | Deadpool 2                 | 2018 | 119     | 7.7  | 66.0      | 480793  | 324.59        |
| ...| ...                        | ...  | ...     | ...  | ...       | ...     | ...           |

### Downloads

* [imdb_scraper.py](imdb_scraper.py) - main program that scrapes the IMDb webpages
* [movies.csv](movies.csv) - outputted csv file

## Built With

* [Requests](https://requests.readthedocs.io) - library for making HTTP requests
* [Beautiful Soup 4](https://pypi.org/project/beautifulsoup4/) - library for scraping information from web pages
* [NumPy](https://numpy.org) - high performance library for multi-dimensional arrays
* [Pandas](https://pandas.pydata.org) - provides tools for manipulating tables