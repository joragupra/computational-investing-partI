import analyze
import marketsim

def main():
    simulation = marketsim.simulate(1000000, 'homework3_testdata/orders.csv')
    print "==============="
    marketsim.write_simulation_result(simulation, 'homework3_testdata/values.csv')
    fund, benchmark = analyze.analyze('homework3_testdata/values.csv', '$SPX')
    analyze.print_analysis_results(fund, benchmark, '$SPX')

    simulation = marketsim.simulate(1000000, 'homework3_testdata/orders2.csv')
    print "==============="
    marketsim.write_simulation_result(simulation, 'homework3_testdata/values2.csv')
    fund, benchmark = analyze.analyze('homework3_testdata/values2.csv', '$SPX')
    analyze.print_analysis_results(fund, benchmark, '$SPX')

if __name__ == '__main__':
    main()
