import numpy
import scipy.stats as stats
import matplotlib.pyplot as plt
import csv

def load_csv(filename, skip_first_row=True):
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        out = []
        i = 0
        for row in reader:
            if(skip_first_row == True):
                if(i == 0):
                    i = i + 1
                    continue

            out.append(row)
            i = i + 1
        
    return out

def main():
    
    filename = 'iris.csv'
    x = load_csv(filename, False)
    
    xp = []
    for i in range(1, len(x), 1):
        x[i][0] = float(x[i][0])
        x[i][1] = float(x[i][1])
        x[i][2] = float(x[i][2])
        x[i][3] = float(x[i][3])

        xp.append(x[i][0:4])
    xp = numpy.asarray(xp, dtype='float32')
    #print(xp)
    x_setosa = xp [0:50,:]
    x_versicolor = xp [50:100,:]
    x_virginica = xp [100:150,:]

    plt.clf()
    plt.figure(figsize=(8,8))
    plt.scatter(
        x_setosa[:,0],
        x_setosa[:,3],
        facecolor=(1,0,0),
        s=20.0,
        label='Setosa',       
    )
    plt.scatter(
        x_versicolor[:,0],
        x_versicolor[:,3],
        facecolor=(0,1,0),
        s=20.0,
        label='versicolor',       
    )
    plt.scatter(
        x_virginica[:,0],
        x_virginica[:,3],
        facecolor=(0,0,1),
        s=20.0,
        label='virginica',       
    )
    plt.tight_layout()
    plt.savefig('scatter1.png', dpi=200)
    plt.show()
    
if __name__ == '__main__':
    main()