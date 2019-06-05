
#Name:Cihat Bostancı
#ID : 150160542

import numpy as np
import sys
import matplotlib.pyplot as plt



def functionA(inSample1,x,inSample2,y):
    f, (ax1, ax2) = plt.subplots(1, 2,sharey=True)

    markerline, stemlines, baseline = ax1.stem( x,inSample1, '-.')
    plt.setp(baseline, 'color', 'r', 'linewidth', 3)
    plt.ylabel("y[n]")
    plt.xlabel("[n]")


    markerline, stemlines, baseline = ax2.stem(y,inSample2, '-.')
    plt.setp(baseline, 'color', 'r', 'linewidth', 3)
    plt.ylabel("y[n]")
    plt.xlabel("[n]")
    plt.show()

if __name__ == '__main__':

    xRangeFrom = int(sys.argv[1])
    xRangeTo = int(sys.argv[2])
    xRangeTo = xRangeTo+1

    yRangeFrom = int(sys.argv[3])
    yRangeTo = int(sys.argv[4])
    yRangeTo = yRangeTo+1

    xSlice = []
    x = []
    ySlice = []
    y = []

    counter = 4

    for i in range(xRangeFrom, xRangeTo):
        xSlice.append(i)
        counter = counter+1
        x.append(int(sys.argv[counter]))


    for j in range(yRangeFrom, yRangeTo):
        ySlice.append(j)
        counter = counter + 1
        y.append(int(sys.argv[counter]))


    xnp = np.array(x)
    xSlicenp = np.array(xSlice)
    ynp = np.array(y)
    ySlicenp = np.array(ySlice)

    functionA(xnp, xSlicenp, ynp, ySlicenp)






