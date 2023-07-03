import csv
import pandas
import numpy

def main():
    filename = 'pop_num_by_age_2563.csv'
    '''
    df = pandas.read_csv(
        filename,
        header=0,
        sep=',',
        lineterminator='\n')
    '''
    '''
    with open(filename, 'r', encoding='utf-8')as file:
        reader = csv.reader(file)
        out = []
        i = 0
        for row in reader:
            if(i > 0):
                out.append(row)
            i = i +1
            print(out)
    '''
    #num_pop = df.iloc[:, 5] *1000.0
    #print(df)
    #print( df.iloc[0:10 ,5] * 1000.0 )
    print( numpy.std(num_pop))

if __name__ =='__main__':
    main()