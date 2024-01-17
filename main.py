from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# GETTING FIN VIZ ARTICLE DATA

news_tables = {}
finvizurl = "https://finviz.com/quote.ashx?t="

tickers = ['AMZN', 'AAMC', 'PHUN', 'AMD', 'FB', 'AMJ']

for ticker in tickers:
    url = finvizurl + ticker
    # request data from the url
    req = Request(url=url, headers={'user-agent': 'my-app'})
    page = urlopen(req)  # open the request
    html = BeautifulSoup(page, 'html.parser')

    # take all the news tables pass them by ids and add the data to a dictionary
    # use beautiful soup syntac to get the table

    news_table = html.find(id='news-table')
    news_tables[ticker] = news_table

    break # be sure to remove so you be able to visualize all stocks

# MANIPULATING FIN VIZ DATA
parsed_data = []

for ticker, news_table in news_tables.items():

    for row in news_table.findAll('tr'):

        title = row.a.text
        date_data = row.td.text.split(" ")

        # ref to the len of date_data, if len == 1, thts the time else splits the date and time
        if len(date_data) == 1:
            time = date_data[0]
        else:
            date = date_data[0]
            time = date_data[1]

        parsed_data.append([ticker, date, time, title])

# APPLYING SENTIMENT ANALYSIS USING NLTK VADER
# on the titles we got from the parsed data (titles)

# create a data frame
df = pd.DataFrame(parsed_data, columns=['ticker', 'date', 'time', 'title'])

# initialize vader
vader = SentimentIntensityAnalyzer()

# create a new column called compound apply vader.polarity fxn on the title column
f = lambda title: vader.polarity_scores(title)['compound']
df['compound'] = df['title'].apply(f)

print(df.head())

# VISUALIZATION OF SENTIMENT ANALYSIS
# trend over time how these companies have been faring
# convert the date from a string to recognizable time format to have a hierachy

df['date'] = pd.to_datetime(df['date'], errors='coerce').dt.date
plt.figure(figsize=(10, 8))

# take all the compound scores and get the average of them daily
# our goal is to know if the day was positive or negative or neutral
mean_df = df.groupby(['ticker', 'date']).mean()

# unstack this data
plt.figure(figsize=(10, 8))
mean_df = mean_df.unstack()
mean_df = mean_df.xs('compound', axis="columns").transpose()
print(mean_df)
mean_df.plot(kind='bar')
plt.show()
