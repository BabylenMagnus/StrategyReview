import pandas as pd


figi = pd.read_excel('figi ticker.xlsx')


def figi_from_ticker(ticker: str):
    ans = figi['figi'][figi['ticker'] == ticker.upper()]

    if len(ans):
        return ans.item()
