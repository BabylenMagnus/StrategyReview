from strategy import BaseStrategy


class Pages:
    index = 'index.html'
    redir = 'redir.html'


class Saves:
    stock_plot = 'static/img/stocks'
    brief_plot = 'static/img/briefs'
    alg_plot = 'static/img/alg'


STRATEGY_DICT = {
    'Base': BaseStrategy
}