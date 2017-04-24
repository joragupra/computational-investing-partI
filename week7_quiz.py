import datetime as dt
import datautils as du
import numpy as np
import pandas as pd
import techanalysis as ta

dt_start = dt.datetime(2010, 1, 1)
dt_end = dt.datetime(2010, 12, 31)
ls_symbols = ['AAPL', 'MSFT']

d_data = du.get_data(dt_start, dt_end, ls_symbols)

look_back_days = 20
df_actual_close = d_data['actual_close']

apple = ta.calculate_bollinger_data(df_actual_close['AAPL'], look_back_days)
microsoft = ta.calculate_bollinger_data(df_actual_close['MSFT'], look_back_days)

def question1():
    q = """
    What is the Bollinger value for AAPL on 2010/5/12 ?
    Lookback = 20 days
    Bollinger_val = (price - rolling_mean) / (rolling_std)
    Please use pandas rolling mean and standard deviation functions.

    * 0.45 to 0.55
    * 0.65 to 0.75
    * 0.75 to 0.85
    * 0.55 to 0.65
    """

    return q, apple['bollinger'][dt.datetime(2010, 5, 12) + dt.timedelta(hours=16)]

def question2():
    q = """
    What is the Bollinger value for AAPL on 2010/5/21 ?
    Lookback = 20 days
    Bollinger_val = (price - rolling_mean) / (rolling_std)
    Please use pandas rolling mean and standard deviation functions.

    * -1.4 to -1.5
    * -1.3 to -1.4
    * -1.2 to -1.3
    * -1.1 to -1.2
    """

    return q, apple['bollinger'][dt.datetime(2010, 5, 21) + dt.timedelta(hours=16)]

def question3():
    q = """
    What is the Bollinger value for AAPL on 2010/6/14 ?
    Lookback = 20 days
    Bollinger_val = (price - rolling_mean) / (rolling_std)
    Please use pandas rolling mean and standard deviation functions.

    * 0.3 to 0.4
    * 0.2 to 0.3
    * 0.4 to 0.5
    * 0.5 to 0.6
    """

    return q, apple['bollinger'][dt.datetime(2010, 6, 14) + dt.timedelta(hours=16)]

def question4():
    q = """
    What is the Bollinger value for AAPL on 2010/6/23 ?
    Lookback = 20 days
    Bollinger_val = (price - rolling_mean) / (rolling_std)
    Please use pandas rolling mean and standard deviation functions.

    * 1.15 to 1.25
    * 0.95 to 1.05
    * 1.35 to 1.45
    * 1.05 to 1.15
    """

    return q, apple['bollinger'][dt.datetime(2010, 6, 23) + dt.timedelta(hours=16)]

def question5():
    q = """
    What is the Bollinger value for MSFT on 2010/5/12 ?
    Lookback = 20 days
    Bollinger_val = (price - rolling_mean) / (rolling_std)
    Please use pandas rolling mean and standard deviation functions.

    * -0.6 to -0.7
    * -0.8 to -0.9
    * -0.7 to -0.8
    * -0.9 to -1.0
    """

    return q, microsoft['bollinger'][dt.datetime(2010, 5, 12) + dt.timedelta(hours=16)]

def question6():
    q = """
    What is the Bollinger value for MSFT on 2010/5/21 ?
    Lookback = 20 days
    Bollinger_val = (price - rolling_mean) / (rolling_std)
    Please use pandas rolling mean and standard deviation functions.

    * 0.9 to 1.0
    * -2.05 to -2.15
    * -1.85 to -1.95
    * -1.95 to -2.05
    """

    return q, microsoft['bollinger'][dt.datetime(2010, 5, 21) + dt.timedelta(hours=16)]

def question7():
    q = """
    What is the Bollinger value for MSFT on 2010/6/14 ?
    Lookback = 20 days
    Bollinger_val = (price - rolling_mean) / (rolling_std)
    Please use pandas rolling mean and standard deviation functions.

    * -0.6 to -0.7
    * -0.5 to -0.6
    * -0.7 to -0.8
    * -0.4 to -0.5
    """

    return q, microsoft['bollinger'][dt.datetime(2010, 6, 14) + dt.timedelta(hours=16)]

def question8():
    q = """
    What is the Bollinger value for MSFT on 2010/6/23 ?
    Lookback = 20 days
    Bollinger_val = (price - rolling_mean) / (rolling_std)
    Please use pandas rolling mean and standard deviation functions.

    * -0.55 to -0.65
    * -0.45 to -0.55
    * -0.35 to -0.45
    * -0.75 to -0.85
    """

    return q, microsoft['bollinger'][dt.datetime(2010, 6, 23) + dt.timedelta(hours=16)]

def main():
    questions = [question1, question2, question3, question4, question5, question6, question7, question8]
    for i in range(0, 8):
        q, ans = questions[i]()
        print '==========================='
        print q
        print ans

if __name__ == '__main__':
    main()
