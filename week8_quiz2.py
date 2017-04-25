import datetime as dt
import techanalysis as ta
import datautils as du
import numpy as np
import pandas as pd
import events as ev

import marketsim as mksim
import analyze as an

def question1():
    q = """
    The event is defined as when :
    Bollinger value of equity today < -2.
    Bollinger value of equity yesterday >= -2.0
    Bollinger value of SPY today >= 1.4

    * Test this event using the Event Profiler over the period from 1st Jan, 2008 to 31st Dec 2009.
    * Using the symbol list - SP5002012
    * Using adjusted_close to create Bollinger bands
    * 20 day lookback Bollinger bands
    * Starting Cash: $100,000
    * At every event Buy 100 shares of the equity, and Sell them 5 trading days later. In case not enough days are available Sell them on the last trading day. (Similar to what the homework 4 description wanted).
    * Run this in your simulator and analyze the results.

    What is the sharpe ratio of the fund ?
    * 0.4 - 0.5
    * 0.5 - 0.6
    * 0.6 - 0.7
    * 0.7 - 0.8
    """

    cash = 100000
    dt_start = dt.datetime(2008, 1, 1)
    dt_end = dt.datetime(2009, 12, 31)

    ls_symbols = du.get_symbols_in_year(2012)
    d_data = du.get_data(dt_start, dt_end, ls_symbols)

    df_events = ev.find_bollinger_events(ls_symbols, d_data, -2.0, 1.4)

    order_file = 'bollinger_orders.csv'
    analysis_file = 'values_bollinger_event.csv'
    benchmark_symbol = '$SPX'

    ev.generate_orders(ls_symbols, df_events, order_file)
    simulation_result = mksim.simulate(cash, order_file)
    mksim.write_simulation_result(simulation_result, analysis_file)
    fund, benchmark = an.analyze(analysis_file, benchmark_symbol)

    return q, fund.sharpe

def main():
    questions = [question1]
    for i in range(0, 1):
        q, ans = questions[i]()
        print '==========================='
        print q
        print ans

if __name__ == '__main__':
    main()
