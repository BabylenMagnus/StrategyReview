import backtrader as bt
import backtrader.feeds as btfeeds


class St(bt.Strategy):
    def __init__(self):
        self.sma_slow = bt.indicators.SMA(period=21)
        self.sma_fast = bt.indicators.SMA(period=9)

        self.crossover = bt.indicators.CrossOver(self.sma_fast, self.sma_slow)

        self.data_close = self.datas[0].close

    def log(self, txt, dt=None):
        print(type(self.datas[0]))
        dt = dt or self.datas[0].datetime.time()
        # print(f"{dt.isoformat()}, {txt}")

    def next(self):
        if self.crossover > 0:
            self.log(f"Buy {self.data_close[0]}")
            self.buy()

        elif self.crossover < 0:
            self.log(f"Sell {self.data_close[0]}")
            self.sell()


data = btfeeds.YahooFinanceCSVData(
    dataname='temp/AAPL 2022_04_02 2022_04_08.csv', timeframe=bt.TimeFrame.Minutes,
    compression=5, quicknotify=True
)

cerebro = bt.Cerebro()
cerebro.adddata(data)
cerebro.addstrategy(St)
cerebro.run()
for stratlist in cerebro.runstrats:
    for si, strat in enumerate(stratlist):
        print(strat.datas)

cerebro.plot(style='candlestick')
