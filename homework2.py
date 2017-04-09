import pandas as pd
import numpy as np
import math
import copy
import QSTK.qstkutil.qsdateutil as du
import datetime as dt
import QSTK.qstkutil.DataAccess as da
import QSTK.qstkutil.tsutil as tsu
#import QSTK.qstkstudy.EventProfiler as ep
# changed to a fixed version of EventProfiler
import EventProfiler as ep

def main():
    dt_start = dt.datetime(2008, 1, 1)
    dt_end = dt.datetime(2009, 12, 31)
    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt.timedelta(hours=16))

    dataobj = da.DataAccess('Yahoo')
    ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']

    print "Analyzing 5-dollar events for equities from SP500 2012..."
    ls_2012_symbols = get_symbols_in_year(dataobj, 2012)
    d_2012_data = get_data(dataobj, ldt_timestamps, ls_2012_symbols)
    profile_5_dollar_events(ls_2012_symbols, d_2012_data, 'SP500_2012.pdf')

    print "Analyzing 5-dollar events for equities from SP500 2008..."
    ls_2008_symbols = get_symbols_in_year(dataobj, 2008)
    d_2008_data = get_data(dataobj, ldt_timestamps, ls_2008_symbols)
    profile_5_dollar_events(ls_2008_symbols, d_2008_data, 'SP500_2008.pdf')

def get_symbols_in_year(dataobj, year):
    dataobj = da.DataAccess('Yahoo')

    ls_symbols = dataobj.get_symbols_from_list('sp500' + str(year))
    ls_symbols.append('SPY')

    return ls_symbols

def get_data(dataobj, ldt_timestamps, ls_symbols):
    ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']

    ldf_data = dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
    d_data = dict(zip(ls_keys, ldf_data))

    for s_key in ls_keys:
        d_data[s_key] = d_data[s_key].fillna(method='ffill')
        d_data[s_key] = d_data[s_key].fillna(method='bfill')
        d_data[s_key] = d_data[s_key].fillna(1.0)

    return d_data

def profile_5_dollar_events(ls_symbols, d_data, filename):
    profile_threshold_actual_close_events(ls_symbols, d_data, 5.0, filename)

def profile_threshold_actual_close_events(ls_symbols, d_data, actual_close_threshold, filename):
    df_events = find_price_drop_events(ls_symbols, d_data, actual_close_threshold)
    ep.eventprofiler(df_events, d_data, i_lookback=20, i_lookforward=20,
                s_filename=filename, b_market_neutral=True, b_errorbars=True,
                s_market_sym='SPY')

def initialize_event_dataframe(df_orig):
    df_events = copy.deepcopy(df_orig)
    df_events = df_events * np.NAN
    return df_events

def find_price_drop_events(ls_symbols, d_data, actual_close_threshold):
    ''' Finding events when a stock price moved from above the threshold to below the threshold '''
    df_actual_close = d_data['actual_close']

    df_events = initialize_event_dataframe (df_actual_close)

    # Time stamps for the event range
    ldt_timestamps = df_actual_close.index

    for s_sym in ls_symbols:
        for i in range(1, len(ldt_timestamps)):
            # Calculating the actual close price for this timestamp and the day before
            f_actual_close_price_today = df_actual_close[s_sym].ix[ldt_timestamps[i]]
            f_actual_close_price_yest = df_actual_close[s_sym].ix[ldt_timestamps[i - 1]]

            # Event is found if the symbol has a actual close price today below the threshold
            # while the actual close price yesterday was above the threshold
            if f_actual_close_price_today < actual_close_threshold and f_actual_close_price_yest >= actual_close_threshold:
                df_events[s_sym].ix[ldt_timestamps[i]] = 1

    return df_events

def find_5_dollar_events(ls_symbols, d_data):
    ''' Finding events when a stock price moved from above 5$ to below 5$ '''
    return find_price_drop_events(ls_symbols, d_data, 5.0)

if __name__ == '__main__':
    main()
