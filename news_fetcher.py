import requests
from newsapi import NewsApiClient

# TODO to move to ENV
NEWS_API_KEY = '<KEY>'

# Fetch News
def fetch_news(category, from_date, to_date):
    newsapi = NewsApiClient(api_key=NEWS_API_KEY)
    all_articles = newsapi.get_everything(q=category,
                                          from_param=from_date,
                                          to=to_date,
                                          language='en',
                                          sort_by='relevancy')
    return all_articles['articles']
