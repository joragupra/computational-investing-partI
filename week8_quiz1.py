import datetime as dt
import datautils as du
import events as ev
import EventProfiler as ep

def question1():
    q = """
    The event is defined as when :
    Bollinger value of equity today < -2.0
    Bollinger value of equity yesterday >= -2.0
    Bollinger value of SPY today >= 1.1

    * Test this event using the Event Profiler over the period from 1st Jan, 2008 to 31st Dec 2009.
    * Using the symbol list - SP5002012
    * Using adjusted_close to create Bollinger bands
    * 20 day lookback Bollinger bands

    What is the number of events for the following event ?
    230 - 235
    235 - 240
    225 - 230
    240 - 245
    """

    filename = 'bollinger_events.pdf'

    dt_start = dt.datetime(2008, 1, 1)
    dt_end = dt.datetime(2009, 12, 31)

    ls_2012_symbols = du.get_symbols_in_year(2012)
    d_data = du.get_data(dt_start, dt_end, ls_2012_symbols)

    df_events = ev.find_bollinger_events(ls_2012_symbols, d_data, -2.0, 1.1)
    ep.eventprofiler(df_events, d_data, i_lookback=20, i_lookforward=20,
                s_filename=filename, b_market_neutral=True, b_errorbars=True,
                s_market_sym='SPY')

    # after looking into the generated event report
    return q, '232'

def main():
    questions = [question1]
    for i in range(0, 1):
        q, ans = questions[i]()
        print '==========================='
        print q
        print ans

if __name__ == '__main__':
    main()
