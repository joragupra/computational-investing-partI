import datetime as dt
import techanalysis as ta
import datautils as du
import numpy as np
import pandas as pd

def main():
    dt_start = dt.datetime(2010, 1, 1)
    dt_end = dt.datetime(2010, 12, 31)
    ls_symbols = ['GOOG', 'AAPL', 'IBM', 'MSFT']

    d_data = du.get_data(dt_start, dt_end, ls_symbols)

    look_back_days = 20
    df_actual_close = d_data['actual_close']

    google = ta.calculate_bollinger_data(df_actual_close['GOOG'], look_back_days)
    apple = ta.calculate_bollinger_data(df_actual_close['AAPL'], look_back_days)
    ibm = ta.calculate_bollinger_data(df_actual_close['IBM'], look_back_days)
    microsoft = ta.calculate_bollinger_data(df_actual_close['MSFT'], look_back_days)

    result = pd.concat([apple['bollinger'], google['bollinger'], ibm['bollinger'], microsoft['bollinger']], axis=1)
    result.columns = ['AAPL', 'GOOG', 'IBM', 'MSFT']

    print result[-5:]

if __name__ == '__main__':
    main()
