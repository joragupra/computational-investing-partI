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
import homework2 as hw

def question1():
    q = """
    The event is defined as when the actual close of the stock price drops below $5.00, more specifically, when:
    price[t-1]>=5.0 and price[t]<5.0 an event has occurred on date t.
    * Test this event using the Event Profiler over the period from 1st Jan, 2008 to 31st Dec 2009.
    * Do two runs - Once with SP5002008 and other with SP5002012.
    Which of the two runs gives better results ?
    """

    dt_start = dt.datetime(2008, 1, 1)
    dt_end = dt.datetime(2009, 12, 31)
    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt.timedelta(hours=16))

    dataobj = da.DataAccess('Yahoo')
    ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']

    ls_2012_symbols = hw.get_symbols_in_year(dataobj, 2012)
    d_2012_data = hw.get_data(dataobj, ldt_timestamps, ls_2012_symbols)
    hw.profile_5_dollar_events(ls_2012_symbols, d_2012_data, 'SP500_2012.pdf')

    ls_2008_symbols = hw.get_symbols_in_year(dataobj, 2008)
    d_2008_data = hw.get_data(dataobj, ldt_timestamps, ls_2008_symbols)
    hw.profile_5_dollar_events(ls_2008_symbols, d_2008_data, 'SP500_2008.pdf')

    # after analyzing the results for equities from both years
    return q, 'S&P5002012'

def question2():
    q = """
    The event is defined as when the actual close of the stock price drops below $6.00, more specifically, when:
    price[t-1]>=6.0 and price[t]<6.0 an event has occurred on date t.
    * Test this event using the Event Profiler over the period from 1st Jan, 2008 to 31st Dec 2009.
    * Using the symbol list - SP5002008
    What is the number of events for the following event ?
    """
    dt_start = dt.datetime(2008, 1, 1)
    dt_end = dt.datetime(2009, 12, 31)
    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt.timedelta(hours=16))

    dataobj = da.DataAccess('Yahoo')
    ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']

    ls_2008_symbols = hw.get_symbols_in_year(dataobj, 2008)
    d_2008_data = hw.get_data(dataobj, ldt_timestamps, ls_2008_symbols)
    hw.profile_threshold_actual_close_events(ls_2008_symbols, d_2008_data, 6.0, 'SP500_2008_6dollar.pdf')

    # after looking into the generated event report
    return q, '386'

def question3():
    q = """
    The event is defined as when the actual close of the stock price drops below $7.00, more specifically, when:
    price[t-1]>=7.0 and price[t]<7.0 an event has occurred on date t.
    * Test this event using the Event Profiler over the period from 1st Jan, 2008 to 31st Dec 2009.
    * Using the symbol list - SP5002008
    What is the number of events for the following event ?
    """

    dt_start = dt.datetime(2008, 1, 1)
    dt_end = dt.datetime(2009, 12, 31)
    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt.timedelta(hours=16))

    dataobj = da.DataAccess('Yahoo')
    ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']

    ls_2008_symbols = hw.get_symbols_in_year(dataobj, 2008)
    d_2008_data = hw.get_data(dataobj, ldt_timestamps, ls_2008_symbols)
    hw.profile_threshold_actual_close_events(ls_2008_symbols, d_2008_data, 7.0, 'SP500_2008_7dollar.pdf')

    # after looking into the generated event report
    return q, '468'

def question4():
    q = """
    The event is defined as when the actual close of the stock price drops below $8.00, more specifically, when:
    price[t-1]>=8.0 and price[t]<8.0 an event has occurred on date t.
    * Test this event using the Event Profiler over the period from 1st Jan, 2008 to 31st Dec 2009.
    * Using the symbol list - SP5002008
    What is the number of events for the following event ?
    """

    dt_start = dt.datetime(2008, 1, 1)
    dt_end = dt.datetime(2009, 12, 31)
    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt.timedelta(hours=16))

    dataobj = da.DataAccess('Yahoo')
    ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']

    ls_2008_symbols = hw.get_symbols_in_year(dataobj, 2008)
    d_2008_data = hw.get_data(dataobj, ldt_timestamps, ls_2008_symbols)
    hw.profile_threshold_actual_close_events(ls_2008_symbols, d_2008_data, 8.0, 'SP500_2008_8dollar.pdf')

    # after looking into the generated event report
    return q, '527'

def question5():
    q = """
    The event is defined as when the actual close of the stock price drops below $9.00, more specifically, when:
    price[t-1]>=9.0 and price[t]<9.0 an event has occurred on date t.
    * Test this event using the Event Profiler over the period from 1st Jan, 2008 to 31st Dec 2009.
    * Using the symbol list - SP5002008
    What is the number of events for the following event ?
    """

    dt_start = dt.datetime(2008, 1, 1)
    dt_end = dt.datetime(2009, 12, 31)
    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt.timedelta(hours=16))

    dataobj = da.DataAccess('Yahoo')
    ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']

    ls_2008_symbols = hw.get_symbols_in_year(dataobj, 2008)
    d_2008_data = hw.get_data(dataobj, ldt_timestamps, ls_2008_symbols)
    hw.profile_threshold_actual_close_events(ls_2008_symbols, d_2008_data, 9.0, 'SP500_2008_9dollar.pdf')

    # after looking into the generated event report
    return q, '596'

def question6():
    q = """
    The event is defined as when the actual close of the stock price drops below $10.00, more specifically, when:
    price[t-1]>=10.0 and price[t]<10.0 an event has occurred on date t.
    * Test this event using the Event Profiler over the period from 1st Jan, 2008 to 31st Dec 2009.
    * Using the symbol list - SP5002008
    What is the number of events for the following event ?
    """

    dt_start = dt.datetime(2008, 1, 1)
    dt_end = dt.datetime(2009, 12, 31)
    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt.timedelta(hours=16))

    dataobj = da.DataAccess('Yahoo')
    ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']

    ls_2008_symbols = hw.get_symbols_in_year(dataobj, 2008)
    d_2008_data = hw.get_data(dataobj, ldt_timestamps, ls_2008_symbols)
    hw.profile_threshold_actual_close_events(ls_2008_symbols, d_2008_data, 10.0, 'SP500_2008_10dollar.pdf')

    # after looking into the generated event report
    return q, '643'

def question7():
    q = """
    The event is defined as when the actual close of the stock price drops below $6.00, more specifically, when:
    price[t-1]>=6.0 and price[t]<6.0 an event has occurred on date t.
    * Test this event using the Event Profiler over the period from 1st Jan, 2008 to 31st Dec 2009.
    * Using the symbol list - SP5002012
    What is the number of events for the following event ?
    """
    dt_start = dt.datetime(2008, 1, 1)
    dt_end = dt.datetime(2009, 12, 31)
    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt.timedelta(hours=16))

    dataobj = da.DataAccess('Yahoo')
    ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']

    ls_2012_symbols = hw.get_symbols_in_year(dataobj, 2012)
    d_2012_data = hw.get_data(dataobj, ldt_timestamps, ls_2012_symbols)
    hw.profile_threshold_actual_close_events(ls_2012_symbols, d_2012_data, 6.0, 'SP500_2012_6dollar.pdf')

    # after looking into the generated event report
    return q, '224'

def question8():
    q = """
    The event is defined as when the actual close of the stock price drops below $7.00, more specifically, when:
    price[t-1]>=7.0 and price[t]<7.0 an event has occurred on date t.
    * Test this event using the Event Profiler over the period from 1st Jan, 2008 to 31st Dec 2009.
    * Using the symbol list - SP5002012
    What is the number of events for the following event ?
    """

    dt_start = dt.datetime(2008, 1, 1)
    dt_end = dt.datetime(2009, 12, 31)
    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt.timedelta(hours=16))

    dataobj = da.DataAccess('Yahoo')
    ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']

    ls_2012_symbols = hw.get_symbols_in_year(dataobj, 2012)
    d_2012_data = hw.get_data(dataobj, ldt_timestamps, ls_2012_symbols)
    hw.profile_threshold_actual_close_events(ls_2012_symbols, d_2012_data, 7.0, 'SP500_2012_7dollar.pdf')

    # after looking into the generated event report
    return q, '282'

def question9():
    q = """
    The event is defined as when the actual close of the stock price drops below $8.00, more specifically, when:
    price[t-1]>=8.0 and price[t]<8.0 an event has occurred on date t.
    * Test this event using the Event Profiler over the period from 1st Jan, 2008 to 31st Dec 2009.
    * Using the symbol list - SP5002012
    What is the number of events for the following event ?
    """

    dt_start = dt.datetime(2008, 1, 1)
    dt_end = dt.datetime(2009, 12, 31)
    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt.timedelta(hours=16))

    dataobj = da.DataAccess('Yahoo')
    ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']

    ls_2012_symbols = hw.get_symbols_in_year(dataobj, 2012)
    d_2012_data = hw.get_data(dataobj, ldt_timestamps, ls_2012_symbols)
    hw.profile_threshold_actual_close_events(ls_2012_symbols, d_2012_data, 8.0, 'SP500_2012_8dollar.pdf')

    # after looking into the generated event report
    return q, '375'

def question10():
    q = """
    The event is defined as when the actual close of the stock price drops below $9.00, more specifically, when:
    price[t-1]>=9.0 and price[t]<9.0 an event has occurred on date t.
    * Test this event using the Event Profiler over the period from 1st Jan, 2008 to 31st Dec 2009.
    * Using the symbol list - SP5002012
    What is the number of events for the following event ?
    """

    dt_start = dt.datetime(2008, 1, 1)
    dt_end = dt.datetime(2009, 12, 31)
    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt.timedelta(hours=16))

    dataobj = da.DataAccess('Yahoo')
    ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']

    ls_2012_symbols = hw.get_symbols_in_year(dataobj, 2012)
    d_2012_data = hw.get_data(dataobj, ldt_timestamps, ls_2012_symbols)
    hw.profile_threshold_actual_close_events(ls_2012_symbols, d_2012_data, 9.0, 'SP500_2012_9dollar.pdf')

    # after looking into the generated event report
    return q, '451'

def question11():
    q = """
    The event is defined as when the actual close of the stock price drops below $10.00, more specifically, when:
    price[t-1]>=10.0 and price[t]<10.0 an event has occurred on date t.
    * Test this event using the Event Profiler over the period from 1st Jan, 2008 to 31st Dec 2009.
    * Using the symbol list - SP5002012
    What is the number of events for the following event ?
    """

    dt_start = dt.datetime(2008, 1, 1)
    dt_end = dt.datetime(2009, 12, 31)
    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt.timedelta(hours=16))

    dataobj = da.DataAccess('Yahoo')
    ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']

    ls_2012_symbols = hw.get_symbols_in_year(dataobj, 2012)
    d_2012_data = hw.get_data(dataobj, ldt_timestamps, ls_2012_symbols)
    hw.profile_threshold_actual_close_events(ls_2012_symbols, d_2012_data, 10.0, 'SP500_2012_10dollar.pdf')

    # after looking into the generated event report
    return q, '461'

def main():
    questions = [question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, question11]
    for i in range(0, 11):
        q, ans = questions[i]()
        print '==========================='
        print q
        print ans

if __name__ == '__main__':
    main()
