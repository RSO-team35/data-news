import os
import httpx
import pandas as pd
import json

key = '603d1e9fa014490496d80e05d2d504c0'
sources = 'ars-technica,crypto-coins-news,engadget,hacker-news,recode,techcrunch,techradar,the-next-web,the-verge,wired'


def get_news(product):
    # get news connected to product
    product = product.replace(" ", "_")
    filename = os.path.join("app", "data", f"articles_{product}.json")

    if not os.path.exists(filename):
        # collect news
        print("No news collected yet")
        f = collect_news(product)
        
    with open(filename, "r") as f:
        articles = json.load(f)

    del articles["content"]
    
    return articles


def collect_news(product):
    # once daily(?) add news to collection for each category
    query = product.replace("_", " ")
    response = httpx.get(f"https://newsapi.org/v2/everything?q={query}&sources={sources}&language=en&sortBy=relevancy&apiKey={key}")
    articles = response.json()["articles"]
    articles = pd.DataFrame.from_records(articles)

    fn = os.path.join("app", "data", f"articles_{product}.json")
    articles.to_json(fn)

    return fn