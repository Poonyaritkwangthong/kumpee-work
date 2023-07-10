import pandas
import numpy
import matplotlib.pyplot as plt
import scipy

def get_normal_dist(x, mu, sigma):
    ''' Get nomal distribution value.
    '''
    a = 1.0/(sigma * numpy.sqrt(2.0 * numpy.pi))    
    b = numpy.exp(-0.5*(((x - mu)/sigma)**2)) 
    y = a * b
    return y

def main():
    n = 10
    x = numpy.arange(-1.0, 1.0, 0.1)
    #print( len(x) )
    y = numpy.zeros(len(x))

    mu = 0.0
    sigma = 0.2

    for i in range(0, len(y), 1):
        y[i] = get_normal_dist(x[i], mu, sigma)
        
    plt.clf()
    plt.plot(
        x,
        y,
        'o-g'
    )
    plt.show()

if __name__=='__main__':
    main()