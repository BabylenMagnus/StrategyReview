import matplotlib.pyplot as plt
from os.path import join

from config import Saves
from utils import get_random_name


def stock_prices(value: 'iterable object',
                 time: 'iterable with time values',
                 path=Saves.stock_plot,
                 window_size: 'Tuple of ints' = (1920, 1080)
                 ):
    name = get_random_name() + '_sp.png'
    fn = join(path, name)

    plt.plot(time, value)

    plt.savefig(fn)
    plt.clf()

    return fn


def brief_count(value: 'iterable object',
                time: 'iterable with time values',
                path=Saves.brief_plot,
                window_size: 'Tuple of ints' = (1920, 1080)
                ):
    name = get_random_name() + '_bp.png'
    fn = join(path, name)

    plt.plot(time, value)

    plt.savefig(fn)
    plt.clf()

    return fn


def alg_plot(value: 'iterable object',
             time: 'iterable with time values',
             path=Saves.alg_plot,
             window_size: 'Tuple of ints' = (1920, 1080)
             ):
    name = get_random_name() + '_ap.png'
    fn = join(path, name)

    plt.plot(time, value)

    plt.savefig(fn)
    plt.clf()

    return fn
