import alpaca_trade_api as api
import yfinance
import pandas as pd
import numpy
from dotenv import load_dotenv, find_dotenv
import os
import asyncio
import aiohttp

load_dotenv()
my_id = os.getenv("API_KEY_ID_Alpaca")
my_secret_key = os.getenv("API_KEY_SECRET_Alpaca")

API_KEY = my_id
API_SECRET = my_secret_key
BASE_URL = "https://paper-api.alpaca.markets"

alpaca_client = api.REST(API_KEY, API_SECRET, BASE_URL)
live_stream_client = api.Stream(API_KEY, API_SECRET)

# Setting parameters before making request
symbol = "BTCUSD"
timeframe = "1Day"
start = "2022-01-01"
end = "2022-01-31"

# Retrieve daily bars for Bitcoin in a DataFrame and printing the first 5 rows
# btc_bars = alpaca_client.get_crypto_bars(symbol, timeframe, start, end).df
# print(btc_bars.head())

# Scraping Historical News
news = alpaca_client.get_news("BTCUSD", start = "2022-07-01", end = "2022-07-10", limit = 50)
# print(news)

list = []
#Getting Dates, Headlines, and Content
for story in news:
    list.append(story.created_at)
    # print(story.headline)
    # print(story.summary)
print(list)
#Scraping Live News
# async def news_data_handler(news):
#     """Will fire each time news data is published"""
#     print(news)

# live_stream_client.subscribe_news(news_data_handler, 'BTCUSD')
# live_stream_client.run()