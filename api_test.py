import requests
from newsapi.newsapi_client import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='c4560a61b5144991b4d60a735e9f5812')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines()

for key, value in top_headlines.items():
    print(key, ' : ', value)