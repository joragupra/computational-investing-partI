import analyze as an
import events as ev
import datetime as dt
import marketsim as mksim
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.DataAccess as da

def main():
    dt_start = dt.datetime(2008, 1, 1)
    dt_end = dt.datetime(2009, 12, 31)
    cash = 50000

    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt.timedelta(hours=16))
    dataobj = da.DataAccess('Yahoo')
    ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']

    ls_2012_symbols = ev.get_symbols_in_year(dataobj, 2012)
    d_2012_data = ev.get_data(dataobj, ldt_timestamps, ls_2012_symbols)

    order_file = 'orders.csv'
    analysis_file = 'values_5_dollar_event.csv'
    benchmark_symbol = '$SPX'

    df_events = ev.find_5_dollar_events(ls_2012_symbols, d_2012_data)
    ev.generate_orders(ls_2012_symbols, df_events, order_file)

    simulation_result = mksim.simulate(cash, order_file)
    mksim.write_simulation_result(simulation_result, analysis_file)

    fund, benchmark = an.analyze(analysis_file, benchmark_symbol)

    fund_value_file_lines = open(analysis_file,'rb').readlines()

    print 'The final value of the portfolio using the sample file is -- %s' % fund_value_file_lines[-1]
    print 'Details of the Performance of the portfolio\n'
    print 'Data Range: %s to %s\n' % (str(dt_start + dt.timedelta(hours=16)), str(dt_end + dt.timedelta(hours=16)))
    print 'Sharpe Ratio of Fund : %.13f' % fund.sharpe
    print 'Sharpe Ratio of $SPX : %.13f\n' % benchmark.sharpe
    print 'Total Return of Fund : %.13f' % fund.total_return
    print 'Total Return of $SPX : %.13f\n' % benchmark.total_return
    print 'Standard Deviation of Fund : %.13f' % fund.std_dev
    print 'Standard Deviation of $SPX : %.13f\n' % benchmark.std_dev
    print 'Average Daily Return of Fund : %.13f' % fund.avg
    print 'Average Daily Return of $SPX : %.13f' % benchmark.avg

if __name__ == '__main__':
    main()
