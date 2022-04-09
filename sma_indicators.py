import backtrader as bt
import backtrader.feeds as btfeeds


class St(bt.Strategy):
    def __init__(self):
        self.sma_slow = bt.indicators.SimpleMovingAverage(self.data, period=200)
        self.sma_norm = bt.indicators.SimpleMovingAverage(self.data, period=21)
        self.sma_fast = bt.indicators.SimpleMovingAverage(self.data, period=9)


data = btfeeds.YahooFinanceCSVData(dataname='temp/AAPL 2022_04_02 2022_04_08.csv', timeframe=bt.TimeFrame.Minutes)

cerebro = bt.Cerebro()
cerebro.adddata(data)
cerebro.addstrategy(St)
cerebro.run()
cerebro.plot(style='candlestick')
