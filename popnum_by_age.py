import csv
import pandas
import numpy

def main():
    filename = 'pop_num_by_age_2563.csv'
    
    df = pandas.read_csv(
        filename,
        header=0,
        sep=',',
        lineterminator='\n')
    
    num_pop_value = df.iloc[0:, 5] * 1000.0
    print('Sum value : {:}'.format(numpy.sum(num_pop_value)))
    print('Maximun value : {:}'.format(numpy.max(num_pop_value)))
    print('minimum value : {:}'.format(numpy.min(num_pop_value)))
    print('Mean value : {:}'.format(numpy.mean(num_pop_value)))
    print('Standard deviation value : {:}'.format(numpy.std(num_pop_value)))
    
    filename = 'pop_num_by_age_province_2563.csv'
    
    dfpv = pandas.read_csv(
        filename,
        header=0,
        sep=',',
        lineterminator='\n')
    
    num_pop_value_province = dfpv.iloc[0:, 5] * 1000.0
    print('Sum value : {:}'.format(numpy.sum(num_pop_value_province)))
    print('Maximun value : {:}'.format(numpy.max(num_pop_value_province)))
    print('minimum value : {:}'.format(numpy.min(num_pop_value_province)))
    print('Mean value : {:}'.format(numpy.mean(num_pop_value_province)))
    print('Standard deviation value : {:}'.format(numpy.std(num_pop_value_province)))
    
    filename = 'pop_num_man_by_age_2563.csv'
    
    dfm = pandas.read_csv(
        filename,
        header=0,
        sep=',',
        lineterminator='\n')
    
    num_pop_man_value = dfm.iloc[0:, 5] * 1000.0
    print('Sum value : {:}'.format(numpy.sum(num_pop_man_value)))
    print('Maximun value : {:}'.format(numpy.max(num_pop_man_value)))
    print('minimum value : {:}'.format(numpy.min(num_pop_man_value)))
    print('Mean value : {:}'.format(numpy.mean(num_pop_man_value)))
    print('Standard deviation value : {:}'.format(numpy.std(num_pop_man_value)))

    filename = 'pop_num_woman_by_age_2563.csv'
    
    dfwm = pandas.read_csv(
        filename,
        header=0,
        sep=',',
        lineterminator='\n')
    
    num_pop_woman_value = dfwm.iloc[0:, 5] * 1000.0
    print('Sum value : {:}'.format(numpy.sum( num_pop_woman_value)))
    print('Maximun value : {:}'.format(numpy.max( num_pop_woman_value)))
    print('minimum value : {:}'.format(numpy.min( num_pop_woman_value)))
    print('Mean value : {:}'.format(numpy.mean( num_pop_woman_value)))
    print('Standard deviation value : {:}'.format(numpy.std( num_pop_woman_value)))
    print('Standard deviation value : {:}'.format(numpy.sum( num_pop_woman_value)+(numpy.std(num_pop_woman_value))))


if __name__ =='__main__':
    main()