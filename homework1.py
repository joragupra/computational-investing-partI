import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da

import datetime as dt
import pandas as pd
import numpy as np
import itertools as it

def main():
    symbols = ['AAPL', 'GLD', 'GOOG', 'XOM']
    port_alloc = [0.4, 0.4, 0.0, 0.2]
    start = dt.datetime(2011, 1, 1)
    end = dt.datetime(2011, 12, 31)
    vol, avg_daily_ret, sharpe, cum_ret = simulate(start, end, symbols, port_alloc)
    print_stats(start, end, symbols, port_alloc, vol, avg_daily_ret, sharpe, cum_ret)

    symbols = ['AXP', 'HPQ', 'IBM', 'HNZ']
    port_alloc = [0.0, 0.0, 0.0, 1.0]
    start = dt.datetime(2010, 1, 1)
    end = dt.datetime(2010, 12, 31)
    vol, avg_daily_ret, sharpe, cum_ret = simulate(start, end, symbols, port_alloc)
    print_stats(start, end, symbols, port_alloc, vol, avg_daily_ret, sharpe, cum_ret)

def print_stats(start, end, symbols, port_alloc, vol, avg_daily_ret, sharpe, cum_ret):
    print '================================='
    print 'Start Date: %s' % start.strftime('%B %d, %Y')
    print 'End Date: %s' % end.strftime('%B %d, %Y')
    print 'Symbols:  %s' % symbols
    print 'Optimal Allocations: %s' % port_alloc
    print 'Sharpe Ratio: %.13f' % sharpe
    print 'Volatility (stdev of daily returns): %.13f' % vol
    print 'Average Daily Return: %.13f' % avg_daily_ret
    print 'Cumulative Return: %.13f' % cum_ret

def simulate(start, end, symbols, port_alloc):
    d_data = load_data(start, end, dt.timedelta(hours=16), symbols)

    prices = d_data['close'].values
    normalized_prices = prices / prices[0,:]

    port_cum_ret = np.sum(normalized_prices * port_alloc, axis=1)
    port_cum_ret_yesterday = np.append([1], port_cum_ret[0:port_cum_ret.shape[0]-1])
    port_daily_ret = np.divide(port_cum_ret, port_cum_ret_yesterday) - 1

    volatility = np.std(port_daily_ret)
    avg_returns = np.average(port_daily_ret)
    sharpe = np.sqrt(252) * avg_returns / volatility
    port_return = port_cum_ret[port_cum_ret.shape[0]-1]

    return volatility, avg_returns, sharpe, port_return

def load_data(start, end, timeofday, symbols):
    timeofday = dt.timedelta(hours=16)
    timestamps = du.getNYSEdays(start, end, timeofday)
    dataobj = da.DataAccess('Yahoo')
    keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
    data = dataobj.get_data(timestamps, symbols, keys)
    return dict(zip(keys, data))

def optimize_portfolio(start, end, symbols):
    best_port_alloc = list(np.zeros(len(symbols)))
    max_sharpe = 0.0
    for port_alloc in generate_alloc(len(symbols)):
        vol, daily_ret, sharpe, cum_ret = simulate(start, end, symbols, port_alloc)
        if sharpe > max_sharpe:
            best_port_alloc = port_alloc
            max_sharpe = sharpe
    return best_port_alloc

def generate_alloc(port_size):
    allocs = []
    possible_allocs = np.asarray(list(it.product([0.0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1.0], repeat=port_size)))
    for possible_alloc in possible_allocs:
        if np.sum(possible_alloc) == 1.0:
            allocs.append(possible_alloc)
    return allocs

if __name__ == '__main__':
    main()
