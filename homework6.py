import datetime as dt
import datautils as du
import events as ev
#import QSTK.qstkstudy.EventProfiler as ep
# changed to a fixed version of EventProfiler
import EventProfiler as ep

def main():
    filename = 'bollinger_events.pdf'

    dt_start = dt.datetime(2008, 1, 1)
    dt_end = dt.datetime(2009, 12, 31)

    ls_2012_symbols = du.get_symbols_in_year(2012)
    d_data = du.get_data(dt_start, dt_end, ls_2012_symbols)

    df_events = ev.find_bollinger_events(ls_2012_symbols, d_data, -2.0, 1.0)
    ep.eventprofiler(df_events, d_data, i_lookback=20, i_lookforward=20,
                s_filename=filename, b_market_neutral=True, b_errorbars=True,
                s_market_sym='SPY')

if __name__ == '__main__':
    main()
