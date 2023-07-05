import numpy

def main():
    a = [
        [0,1,2,3],
        [4,5,6,7],
        [8,9,10,11]
    ]
    a = numpy.asarray(a)
    #a = a[2,:]
    a = a / 2.0
    
    print(a)
    #print('Minimum value : {:}'.format(numpy.min(a,0)))
    #print('Maximum value : {:}'.format(numpy.max(a)))
    #print('Sum value : {:}'.format(numpy.sum(a)))
    #print('Mean value : {:}'.format(numpy.mean(a)))

if __name__ == '__main__':
    main()