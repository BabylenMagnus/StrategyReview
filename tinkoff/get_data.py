import pandas as pd
import tinvest


async def get_trade_instruments(client: tinvest.AsyncClient):
    """
    если нужны все инструменты на рынке (акции, облигации, индексы...)
    воспользуйся этой функцией. Но не забудь передать client, которые ты
    обязан был создать, когда работаешь с tininvest, сэндбокс клиент
    создаётся в autorization модуле.
    Данные возвращаються в pandas формате, внутри которого всё лежит
    в numpy массивах, потомучто так работает Pandas и Python.
    А в другом формате данные нам нахуй не нужны.
    """
    res = await client.get_market_stocks()

    names = []
    min_price_increment = []
    ticker = []
    types = []
    currency = []

    for instrument in res.payload.instruments:
        names.append(instrument.name)
        min_price_increment.append(instrument.min_price_increment)
        ticker.append(instrument.ticker)
        types.append(instrument.type.name)
        currency.append(instrument.currency.name)

    d = {
        'Name': names,
        'ticker': ticker,
        'types': types,
        'min_price': min_price_increment,
        'currency': currency
    }

    return pd.DataFrame(data=d)
