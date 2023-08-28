import numpy
import matplotlib.pyplot as plt

def main():
    
    a = [29.32, 0.20, 0.41, 0.07, 4.34, 21.64, 0.07, 0.02, 0.24, 40.65, 0.09, 0.98, 0.01, 0.08, 0.02, 0.23, 0.03, 0.02, 0.03, 0.08, 0.43, 0.02, 0.01, 0.01, 0.03, 0.40, 0.02, 0.01, 0.03, 0.34, 0.02, 0.01, 0.02, 0.01, 0.01, 0.03, 0.02, 0.00, 0.02, 0.03]
    a = numpy.asarray(a)
    
    b = [0.00, 20.00, 40.00, 60.00, 80.00, 100.00]
    b = numpy.asarray(b)
    
    plt.clf()
    plt.plot(
        b,
        '.w'
    )
    plt.plot(
        a,
        
        'or'
    )
    plt.plot(
        a,
        
        ':g'
    )
    plt.show()

if __name__ =='__main__':
    main()