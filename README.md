# Sentiment-Analysis-and-Visualization-of-Stock-News
To understand financial news and make the decision on stocks, every day authors around the world post articles on FINVIZ.com. To see all articles, FINVIZ.com is best.
To understand whether its positive or negative news, we use a model to parse Finviz.com, gather all articles titles and use sentiment analysis to understand if averagely per day the news is positive or negative.

# Financial News Sentiment Analysis

## Overview

This project focuses on performing sentiment analysis on financial news articles for selected stocks using Python and NLTK's VADER sentiment analysis tool. The goal is to gain insights into the overall sentiment trends for different stocks over time.

## Data Source

- The financial news articles were obtained from [Finviz](https://finviz.com/quote.ashx?t=).
- Stocks analyzed: $AMZN, $AAMC, $PHUN, $AMD, $FB, $AMJ.

## Project Structure

- **`main.py`**: The main Python script containing the entire sentiment analysis workflow.
- **`requirements.txt`**: A file specifying the project dependencies.
- **`README.md`**: This file, providing an overview of the project.

## Steps

1. **Data Retrieval:**
   - Utilized Finviz to obtain financial news articles for the selected stocks.
   - Web Scraping
   - Extracted relevant information using BeautifulSoup.

2. **Sentiment Analysis:**
   - Applied NLTK VADER for sentiment analysis on the article headlines.
   - Calculated the compound sentiment score for each article.

3. **Data Visualization:**
   - Plotted sentiment trends over time using matplotlib and seaborn.
   - Created bar charts to visualize average daily sentiment scores.

## Key Insights

- Positive sentiment spikes may correlate with favorable news or market performance.
- Negative sentiment periods might indicate challenges or concerns in the market.

## How to Run

1. Install dependencies: `pip install -r requirements.txt`
2. Run the script: `python main.py`

## Visualization

![Sentiment Trends](path/to/sentiment_trends.png)

## Conclusion

This project offers a comprehensive analysis of sentiment trends in financial news articles, providing valuable insights for understanding market sentiments related to the selected stocks.

Feel free to explore the code, run the analysis, and share your observations!
