import numpy
import scipy.stats as stats
import matplotlib.pyplot as plt
import csv

def main():
    alpha = 0.05
    mu    = 100

    # The data : mean of ....
    pre  = [88, 82, 84, 93, 75, 78, 84, 87, 95, 91, 83, 89, 77, 68, 91]
    post = [91, 84, 88, 90, 79, 80, 88, 90, 90, 96, 88, 89, 81, 74, 92]


    # Calculate t-test
    ret = stats.ttest_rel(
        pre,    # an array of sample observations for group 1
        post,   # an array of sample observations for group 1
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