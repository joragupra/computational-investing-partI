import pandas as pd
import numpy as np
import math
import copy
import datetime as dt
#import QSTK.qstkstudy.EventProfiler as ep
# changed to a fixed version of EventProfiler
import EventProfiler as ep
import datautils as du
import events as ev

def main():
    dt_start = dt.datetime(2008, 1, 1)
    dt_end = dt.datetime(2009, 12, 31)

    ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']

    print "Analyzing 5-dollar events for equities from SP500 2012..."
    ls_2012_symbols = du.get_symbols_in_year(2012)
    d_2012_data = du.get_data(dt_start, dt_end, ls_2012_symbols)
    ev.profile_threshold_actual_close_events(ls_2012_symbols, d_2012_data, 5.0, 'SP500_2012.pdf')

    print "Analyzing 5-dollar events for equities from SP500 2008..."
    ls_2008_symbols = du.get_symbols_in_year(2008)
    d_2008_data = du.get_data(dt_start, dt_end, ls_2008_symbols)
    ev.profile_threshold_actual_close_events(ls_2008_symbols, d_2008_data, 5.0, 'SP500_2008.pdf')

if __name__ == '__main__':
    main()
