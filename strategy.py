from utils import get_shares
from datetime import date
import pandas as pd
import numpy as np
from typing import Callable


class Strategy:
    history: list
    decision: Callable

    def __init__(self, ticket: str, start_date: date, end_date: date):
        self.data = get_shares(ticket)
        assert not self.data is None, "Wrong ticket"

        start_date = max(self.data.index.min().date(), start_date)
        start_point = self.data[pd.to_datetime(self.data['Date']) >= np.datetime64(start_date)].index[0]
        end_point = self.data[pd.to_datetime(self.data['Date']) <= np.datetime64(end_date)].index[-1]
        self.data = np.array(self.data)[start_point: end_point]

        self.ent_point = 0
        self.close_point = 0
        self.amount = .5

        self.min_per = .1

        self.history = []

    def simulation(self):
        open, high, low, close, current_date = self.data[0]

        self.ent_point = high

        for open, high, low, close, current_date in self.data[1:]:
            self.decision(open, high, low, close)

    def buy(self, stock, price):
        if self.amount == 1:
            return

        self.amount += stock

        if self.amount > 1:
            stock -= self.amount - 1
            self.amount = 1

        self.history.append(['Buy', stock, price])

    def sold(self, stock, price):
        if self.amount == 0:
            return

        self.amount -= stock

        if self.amount < 0:
            stock += self.amount
            self.amount = 0

        self.history.append(['Sold', stock, price])


class BaseStrategy(Strategy):
    past: int

    def __init__(self, ticket: str, start_date: date):
        super(Strategy).__init__(ticket, start_date)

        self.close_down_age = 0

    def decision(self, open, high, low, close):
        if self.past > close:
            self.close_down_age += 1
        elif self.close_down_age > 2:
            self.amount += self.min_per
            self.amount = max()
        else:
            self.close_down_age = 0
