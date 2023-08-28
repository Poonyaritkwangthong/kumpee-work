import numpy
import scipy.stats as stats
import matplotlib.pyplot as plt
import csv

def main():
    alpha = 0.05
    mu    = 100

    # The data : mean of a heights of ...
    group1 = numpy.array([
        14, 15, 15, 16, 13, 
        8,  14, 17, 16, 14,
        19, 20, 21, 15, 15, 
        16, 16, 13, 14, 12])
    group2 = numpy.array([
        15, 17, 14, 17, 14,
         8, 12, 19, 19, 14, 
        17, 22, 24, 16, 13, 
        16, 13, 18, 15, 13])


    # Calculate t-test
    ret = stats.ttest_ind(
        group1,     # an array of sample observations for group 1
        group2,     # an array of sample observations for group 2
        equal_var=True)
    p_value = ret.pvalue
 
    print('P-value: {:.2f}'.format(p_value))

    # Make decision
    if(p_value < alpha):
        print('Accept H1')
    else:
        print('Accept H0')

if __name__ == '__main__':
    main()