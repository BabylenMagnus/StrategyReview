import os.path
import random

import pandas as pd
import yfinance as yf
from datetime import date


figi = pd.read_excel('figi ticker.xlsx')
tickers = list(figi['ticker'])
start_date = "2000-01-01"


def figi_from_ticker(ticker: str):
    ans = figi['figi'][figi['ticker'] == ticker.upper()]

    if len(ans):
        return ans.item()


def get_shares(ticker: str):
    ticker = ticker.upper()
    if ticker not in tickers:
        return
    name = os.path.join("temp", f"{ticker}.csv")

    if name in os.listdir('temp'):
        data = pd.read_csv(name)
    else:
        data = yf.download(ticker, start_date, date.today().strftime("%Y-%m-%d"))
        data.to_csv(name)
        data.drop(columns=['Adj Close', 'Volume'], inplace=True)
        data['Date'] = data.index
        data.reset_index(drop=True, inplace=True)

    return data


def get_random_name(n=7):
    return str(random.random())[-n:]
