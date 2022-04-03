import os.path
import random

import pandas as pd
import yfinance as yf
from datetime import date, datetime
import numpy as np

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

    if os.path.isfile(name):
        data = pd.read_csv(name)
    else:
        data = yf.download(ticker, start_date, date.today().strftime("%Y-%m-%d"))
        data.drop(columns=['Adj Close', 'Volume'], inplace=True)
        data['Date'] = data.index
        data.reset_index(drop=True, inplace=True)
        data.to_csv(name, index=False)
        data = pd.read_csv(name)

    return data


def get_close_series(ticket, start_date, end_date):
    data = get_shares(ticket)
    assert not data is None, "Wrong ticket"

    start_date = max(datetime.strptime(data['Date'][0], '%Y-%m-%d'), start_date)
    start_point = data[pd.to_datetime(data['Date']) >= np.datetime64(start_date)].index[0]
    end_point = data[pd.to_datetime(data['Date']) <= np.datetime64(end_date)].index[-1]
    data = np.array(data)
    iter_data = data[start_point: end_point, 3]
    return iter_data


def get_random_name(n=7):
    return str(random.random())[-n:]


str2date = lambda n: datetime.strptime(n, "%Y-%m-%d")
