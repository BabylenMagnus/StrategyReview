from utils import get_shares
from datetime import date
from datetime import datetime, time
import pandas as pd
import numpy as np
from typing import Callable


class Strategy:
    history: list
    decision: Callable
    start: Callable
    current_date: date

    def __init__(self, ticket: str, start_date: date, end_date: date):
        start_date = datetime.combine(start_date, time(0, 0))
        self.data = get_shares(ticket)
        assert not self.data is None, "Wrong ticket"

        start_date = max(datetime.strptime(self.data['Date'][0], '%Y-%m-%d'), start_date)
        self.start_point = self.data[pd.to_datetime(self.data['Date']) >= np.datetime64(start_date)].index[0]
        self.end_point = self.data[pd.to_datetime(self.data['Date']) <= np.datetime64(end_date)].index[-1]
        self.data = np.array(self.data)
        self.iter_data = self.data[self.start_point: self.end_point]

        self.ent_point = 0
        self.close_point = 0
        self.amount = .0

        self.history = []

    def simulation(self):
        open, high, low, close, current_date = self.iter_data[0]
        self.current_date = current_date
        self.ent_point = high
        self.start(open, high, low, close)
        
        for open, high, low, close, current_date in self.iter_data[1:-1]:
            self.current_date = current_date
            self.decision(open, high, low, close)

        open, high, low, close, current_date = self.iter_data[-1]

        return self.history, self.amount, close

    def buy(self, stock: float, price: float):
        if self.amount == 1:
            return

        self.amount += stock

        if self.amount > 1:
            stock -= self.amount - 1
            self.amount = 1

        self.history.append(['Buy', self.current_date, stock, price])

    def count_bills(self, start_bills):
        bills = start_bills
        num_shares = 0
        value_in_shares = 0
        num_buy = 0
        for action, operation_date, stonks, price in self.history:
            if action == "Buy":
                transaction = bills * stonks
                bills -= transaction
                num_shares += transaction / price
                num_buy += 1
            else:
                value_in_shares = num_shares * price
                transaction = value_in_shares / num_buy
                bills += transaction
                value_in_shares -= transaction

        return bills

    def sold(self, stock, price):
        if self.amount == 0:
            return

        self.amount -= stock

        if self.amount < 0:
            stock += self.amount
            self.amount = 0

        self.history.append(['Sold', self.current_date, stock, price])


class BaseStrategy(Strategy):

    def __init__(
            self, ticket: str, start_date: date, end_date: date, exit_value=0.1, day_ruin=0.02, days2out=12,
            buy_past_days_down=2, close_past_days=3
    ):
        super().__init__(ticket, start_date, end_date)
        self.st_stock = .1
        self.amount = 0

        self.value_down_days = 0
        self.close_up_days = 0

        self.past = 0
        self.past = 0

        self.next_day_sold = False

        self.day_in_row = 0

        self.exit_value = exit_value
        self.day_ruin = day_ruin
        self.days2out = days2out
        self.buy_past_days_down = buy_past_days_down
        self.close_past_days = close_past_days

    def start(self, open, high, low, close):
        self.past = close
        value = (open + close) / 2

        self.buy(1, value)

    def decision(self, open, high, low, close):

        if self.day_in_row == self.days2out:
            self.sold(1, close)

        if ((self.past - low) / self.past) < -self.exit_value:
            self.sold(1, close)

        if self.next_day_sold:
            self.sold(self.st_stock, close)
            self.next_day_sold = False

        value = (open + close) / 2

        if self.past >= value:
            self.value_down_days += 1
        else:
            self.value_down_days = 0

        if close > self.past:
            self.close_up_days += 1
        else:
            self.close_up_days = 0

        if self.value_down_days >= self.buy_past_days_down and self.past <= value:
            self.buy(self.st_stock, close)
        elif self.amount > 0 and self.close_up_days > self.close_past_days and \
                ((self.past - low) / self.past) < -self.day_ruin:
            self.next_day_sold = True

        self.past = close

        if self.amount > 0:
            self.day_in_row += 1
        else:
            self.day_in_row = 0


class MeanReversion(Strategy):
    def __init__(self, ticket: str, start_date: date, end_date: date, n_days_view=12, percent_ind_trend=0.01):
        super().__init__(ticket, start_date, end_date)

        self.current_point = self.start_point
        self.n_days_veiw = n_days_view
        self.percent_ind_trend = percent_ind_trend

        self.st_stock = .1

    def start(self, open, high, low, close):
        self.decision(open, high, low, close)

    def decision(self, open, high, low, close):
        period = self.data[max(self.current_point - self.n_days_veiw, 0): self.current_point, 3]
        value = close / period[0]

        # trend_up = value > 1 + self.percent_ind_trend
        # trend_down = value < 1 - self.percent_ind_trend

        if close <= min(period):
            self.buy(self.st_stock, close)
        if close >= max(period):
            self.sold(self.st_stock, close)

        self.current_point += 1
