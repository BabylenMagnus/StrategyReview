from utils import get_shares
from datetime import date
import pandas as pd
import numpy as np
from typing import Callable


class Strategy:
    history: str
    decision: Callable

    def __init__(self, ticket: str, start_date: date, balance=10000):
        self.data = get_shares(ticket)
        assert len(self.data) == 0, "Wrong ticket"
        self.start_date = max(self.data.index.min().date(), start_date)
        self.start_point = self.data[pd.to_datetime(self.data['Date']) >= np.datetime64(start_date)].index[0]
        self.data = np.array(self.data)[self.start_point]

        self.balance = balance

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
        self.amount += stock


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
