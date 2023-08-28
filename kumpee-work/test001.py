import numpy
import scipy.stats as stats
import matplotlib.pyplot as plt
import csv

def main():
    alpha = 0.05
    mu    = 100

    # The data : mean of a heights of ...
    data = [
        150, 100, 200,
        150,  50,  50, 
         50,  50, 100,
        100, 100, 200,
        200, 100]

    # Calculate t-test
    ret = stats.ttest_1samp(
        a=data,
        popmean=mu
    )
    p_value = ret.pvalue
 
    print('P-value: {:.2f}'.format(p_value))

    # Make decision
    if(p_value < alpha):
        print('Accept H1')
    else:
        print('Accept H0')

if __name__ == '__main__':
    main()