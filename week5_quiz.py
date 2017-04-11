import datetime as dt
import marketsim

def question1():
    q = """
    Run your market simulator on Orders.csv.
    What is the value of the portfolio on 6th December, 2011 ?
    * 1126000.0 to 1128000.0
    * 1122000.0 to 1124000.0
    * 1124000.0 to 1126000.0
    * 1128000.0 to 1130000.0
    """

    simulation_result = marketsim.simulate(1000000, 'orders_quiz.csv')

    return q, simulation_result['portfolio_value'][dt.datetime(2011, 12, 6) + dt.timedelta(hours=16)]

def question2():
    q = """
    Run your market simulator on Orders.csv.
    What is the value of the portfolio on 9th November, 2011 ?
    * 1130000.0 to 1132000.0
    * 1136000.0 to 1138000.0
    * 1132000.0 to 1134000.0
    * 1134000.0 to 1136000.0
    """

    simulation_result = marketsim.simulate(1000000, 'orders_quiz.csv')

    return q, simulation_result['portfolio_value'][dt.datetime(2011, 11, 9) + dt.timedelta(hours=16)]

def question3():
    q = """
    Run your market simulator on Orders.csv.
    What is the value of the portfolio on 26th September, 2011 ?
    * 1142000.0 to 1144000.0
    * 1146000.0 to 1148000.0
    * 1144000.0 to 1146000.0
    * 1140000.0 to 1142000.0
    """

    simulation_result = marketsim.simulate(1000000, 'orders_quiz.csv')

    return q, simulation_result['portfolio_value'][dt.datetime(2011, 9, 26) + dt.timedelta(hours=16)]

def question4():
    q = """
    Run your market simulator on Orders.csv.
    What is the value of the portfolio on 21st July, 2011 ?
    * 1121000.0 to 1123000.0
    * 1125000.0 to 1127000.0
    * 1127000.0 to 1129000.0
    * 1123000.0 to 1125000.0
    """

    simulation_result = marketsim.simulate(1000000, 'orders_quiz.csv')

    return q, simulation_result['portfolio_value'][dt.datetime(2011, 7, 21) + dt.timedelta(hours=16)]

def question5():
    q = """
    Run your market simulator on Orders.csv.
    What is the value of the portfolio on 28th March, 2011 ?
    * 1052000.0 to 1054000.0
    * 1054000.0 to 1056000.0
    * 1056000.0 to 1058000.0
    * 1050000.0 to 1052000.0
    """

    simulation_result = marketsim.simulate(1000000, 'orders_quiz.csv')

    return q, simulation_result['portfolio_value'][dt.datetime(2011, 3, 28) + dt.timedelta(hours=16)]


def question6():
    q = """
    Run your market simulator on Orders2.csv.
    What is the value of the portfolio on 6th December, 2011 ?
    * 1090000.0 to 1092000.0
    * 1092000.0 to 1094000.0
    * 1094000.0 to 1096000.0
    * 1096000.0 to 1098000.0
    """

    simulation_result = marketsim.simulate(1000000, 'orders_quiz2.csv')

    return q, simulation_result['portfolio_value'][dt.datetime(2011, 12, 6) + dt.timedelta(hours=16)]

def question7():
    q = """
    Run your market simulator on Orders2.csv.
    What is the value of the portfolio on 9th November, 2011 ?
    * 1096000.0 to 1098000.0
    * 1094000.0 to 1096000.0
    * 1090000.0 to 1092000.0
    * 1092000.0 to 1094000.0
    """

    simulation_result = marketsim.simulate(1000000, 'orders_quiz2.csv')

    return q, simulation_result['portfolio_value'][dt.datetime(2011, 11, 9) + dt.timedelta(hours=16)]

def question8():
    q = """
    Run your market simulator on Orders2.csv.
    What is the value of the portfolio on 26th September, 2011 ?
    * 1100000.0 to 1102000.0
    * 1106000.0 to 1108000.0
    * 1102000.0 to 1104000.0
    * 1104000.0 to 1106000.0
    """

    simulation_result = marketsim.simulate(1000000, 'orders_quiz2.csv')

    return q, simulation_result['portfolio_value'][dt.datetime(2011, 9, 26) + dt.timedelta(hours=16)]

def question9():
    q = """
    Run your market simulator on Orders2.csv.
    What is the value of the portfolio on 21st July, 2011 ?
    * 1081000.0 to 1083000.0
    * 1085000.0 to 1087000.0
    * 1087000.0 to 1089000.0
    * 1083000.0 to 1085000.0
    """

    simulation_result = marketsim.simulate(1000000, 'orders_quiz2.csv')

    return q, simulation_result['portfolio_value'][dt.datetime(2011, 7, 21) + dt.timedelta(hours=16)]

def question10():
    q = """
    Run your market simulator on Orders2.csv.
    What is the value of the portfolio on 28th March, 2011 ?
    * 1007000.0 to 1009000.0
    * 1009000.0 to 1011000.0
    * 1003000.0 to 1005000.0
    * 1005000.0 to 1007000.0
    """

    simulation_result = marketsim.simulate(1000000, 'orders_quiz2.csv')

    return q, simulation_result['portfolio_value'][dt.datetime(2011, 3, 28) + dt.timedelta(hours=16)]

def main():
    questions = [question1, question2, question3, question4, question5, question6, question7, question8, question9, question10]
    for i in range(0, 10):
        q, ans = questions[i]()
        print '==========================='
        print q
        print ans

if __name__ == '__main__':
    main()
