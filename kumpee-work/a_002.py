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
    
    filename = 'th_incomes.csv'
    x = load_csv(filename, False)
    
    xp = []
    for i in range(1, len(x), 1):
        x[i][1] = float(x[i][1])
        x[i][2] = float(x[i][2])
        x[i][3] = float(x[i][3])
        x[i][4] = float(x[i][4])
        x[i][5] = float(x[i][5])
        x[i][6] = float(x[i][6])
        x[i][7] = float(x[i][7])
        x[i][8] = float(x[i][8])
        x[i][9] = float(x[i][9])
        x[i][10] = float(x[i][10])


        xp.append(x[i][1:11])
    xp = numpy.asarray(xp, dtype='float32')
    #print(xp)

    data = numpy.transpose(xp)
    labels = [
          'bangkok',
          'chanthaburi',
          'phuket',
    ]

    plt.clf()
    plt.boxplot(
        data,
        labels=None,
        showmeans=True,
        meanline=True,

    )
    plt.tight_layout()
    plt.savefig('th_incomes.png', dpi = 200)
    plt.show()
    
    
if __name__ == '__main__':
    main()