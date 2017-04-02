import datetime as dt
import homework1 as hw

def question1():
    q = """
        The Sharpe ratio of the optimized portfolio using the parameter below lies in the range :
        Equities = ['AAPL', 'GOOG', 'IBM', 'MSFT']
        Start Date = 1st January, 2011
        End Date = 31st December, 2011
        """
    symbols = ['AAPL', 'GOOG', 'IBM', 'MSFT']
    start = dt.datetime(2011, 1, 1)
    end = dt.datetime(2011, 12, 31)
    alloc = hw.optimize_portfolio(start, end, symbols)
    vol, daily_ret, sharpe, cum_ret = hw.simulate(start, end, symbols, alloc)
    return q, 'Sharpe Ratio: %.13f' % sharpe

def question2():
    q = """
        The Sharpe ratio of the optimized portfolio using the parameter below lies in the range :
        Equities = ['BRCM', 'ADBE', 'AMD', 'ADI']
        Start Date = 1st January, 2010
        End Date = 31st December, 2010
        """
    symbols = ['BRCM', 'ADBE', 'AMD', 'ADI']
    start = dt.datetime(2010, 1, 1)
    end = dt.datetime(2010, 12, 31)
    alloc = hw.optimize_portfolio(start, end, symbols)
    vol, daily_ret, sharpe, cum_ret = hw.simulate(start, end, symbols, alloc)
    return q, 'Sharpe Ratio: %.13f' % sharpe

def question3():
    q = """
        The Sharpe ratio of the optimized portfolio using the parameter below lies in the range :
        Equities = ['BRCM', 'TXN', 'AMD', 'ADI']
        Start Date = 1st January, 2011
        End Date = 31st December, 2011
        """
    symbols = ['BRCM', 'TXN', 'AMD', 'ADI']
    start = dt.datetime(2011, 1, 1)
    end = dt.datetime(2011, 12, 31)
    alloc = hw.optimize_portfolio(start, end, symbols)
    vol, daily_ret, sharpe, cum_ret = hw.simulate(start, end, symbols, alloc)
    return q, 'Sharpe Ratio: %.13f' % sharpe

def question4():
    q = """
        The Sharpe ratio of the optimized portfolio using the parameter below lies in the range :
        Equities = ['BRCM', 'TXN', 'IBM', 'HNZ']
        Start Date = 1st January, 2010
        End Date = 31st December, 2010
        """
    symbols = ['BRCM', 'TXN', 'IBM', 'HNZ']
    start = dt.datetime(2010, 1, 1)
    end = dt.datetime(2010, 12, 31)
    alloc = hw.optimize_portfolio(start, end, symbols)
    vol, daily_ret, sharpe, cum_ret = hw.simulate(start, end, symbols, alloc)
    return q, 'Sharpe Ratio: %.13f' % sharpe

def question5():
    q = """
        The Sharpe ratio of the optimized portfolio using the parameter below lies in the range :
        Equities = ['C', 'GS', 'IBM', 'HNZ']
        Start Date = 1st January, 2010
        End Date = 31st December, 2010
        """
    symbols = ['C', 'GS', 'IBM', 'HNZ']
    start = dt.datetime(2010, 1, 1)
    end = dt.datetime(2010, 12, 31)
    alloc = hw.optimize_portfolio(start, end, symbols)
    vol, daily_ret, sharpe, cum_ret = hw.simulate(start, end, symbols, alloc)
    return q, 'Sharpe Ratio: %.13f' % sharpe

def question6():
    q = """
        The Allocations of the optimized portfolio using the parameter below is :
        Equities = ['AAPL', 'GOOG', 'IBM', 'MSFT']
        Start Date = 1st January, 2011
        End Date = 31st December, 2011
        """
    symbols = ['AAPL', 'GOOG', 'IBM', 'MSFT']
    start = dt.datetime(2011, 1, 1)
    end = dt.datetime(2011, 12, 31)
    alloc = hw.optimize_portfolio(start, end, symbols)
    return q, 'Portfolio Allocation: %s' % alloc

def question7():
    q = """
        The Allocations of the optimized portfolio using the parameter below is :
        Equities = ['BRCM', 'ADBE', 'AMD', 'ADI']
        Start Date = 1st January, 2011
        End Date = 31st December, 2011
        """
    symbols = ['BRCM', 'ADBE', 'AMD', 'ADI']
    start = dt.datetime(2011, 1, 1)
    end = dt.datetime(2011, 12, 31)
    alloc = hw.optimize_portfolio(start, end, symbols)
    return q, 'Portfolio Allocation: %s' % alloc

def question8():
    q = """
        The Allocations of the optimized portfolio using the parameter below is :
        Equities = ['BRCM', 'TXN', 'AMD', 'ADI']
        Start Date = 1st January, 2011
        End Date = 31st December, 2011
        """
    symbols = ['BRCM', 'TXN', 'AMD', 'ADI']
    start = dt.datetime(2011, 1, 1)
    end = dt.datetime(2011, 12, 31)
    alloc = hw.optimize_portfolio(start, end, symbols)
    return q, 'Portfolio Allocation: %s' % alloc

def question9():
    q = """
        The Allocations of the optimized portfolio using the parameter below is :
        Equities = ['BRCM', 'TXN', 'IBM', 'HNZ']
        Start Date = 1st January, 2010
        End Date = 31st December, 2010
        """
    symbols = ['BRCM', 'TXN', 'IBM', 'HNZ']
    start = dt.datetime(2010, 1, 1)
    end = dt.datetime(2010, 12, 31)
    alloc = hw.optimize_portfolio(start, end, symbols)
    return q, 'Portfolio Allocation: %s' % alloc

def question10():
    q = """
        The Allocations of the optimized portfolio using the parameter below is :
        Equities = ['C', 'GS', 'IBM', 'HNZ']
        Start Date = 1st January, 2010
        End Date = 31st December, 2010
        """
    symbols = ['C', 'GS', 'IBM', 'HNZ']
    start = dt.datetime(2010, 1, 1)
    end = dt.datetime(2010, 12, 31)
    alloc = hw.optimize_portfolio(start, end, symbols)
    return q, 'Portfolio Allocation: %s' % alloc

def main():
    questions = [question1, question2, question3, question4, question5, question6, question7, question8, question9, question10]
    for i in range(0, 10):
        q, ans = questions[i]()
        print '==========================='
        print q
        print ans

if __name__ == '__main__':
    main()
