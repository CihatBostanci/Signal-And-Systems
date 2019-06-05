import numpy as np
import matplotlib.pyplot as plt
import sys
#Name:Cihat Bostancı
#ID : 150160542
def functionC(x1, y1,sliceData):



    y = []
    for i in range(0, len(x1)):
        y.append(0)
        for j in range(0, len(y1)):

            y[i] += x1[i - j] * y1[j];


    markerline, stemlines, baseline = plt.stem(sliceData ,np.array(y), '-.')
    plt.setp(baseline, 'color', 'r', 'linewidth', 4)
    #plt.title(name)
    plt.ylabel("y[n]")
    plt.xlabel("[n]")
    plt.show()
if __name__ == '__main__':

    xRangeFrom = int(sys.argv[1])
    xRangeTo = int(sys.argv[2])
    xRangeTo = xRangeTo + 1

    yRangeFrom = int(sys.argv[3])
    yRangeTo = int(sys.argv[4])
    yRangeTo = yRangeTo + 1

    xSlice = []
    x = []
    ySlice = []
    y = []

    counter = 4

    for i in range(xRangeFrom, xRangeTo):
        xSlice.append(i)
        counter = counter + 1
        x.append(int(sys.argv[counter]))

    for j in range(yRangeFrom, yRangeTo):
        ySlice.append(j)
        counter = counter + 1
        y.append(int(sys.argv[counter]))

    xnp = np.array(x)
    xSlicenp = np.array(xSlice)
    ynp = np.array(y)
    ySlicenp = np.array(ySlice)

    functionC(xnp, ynp, xSlicenp)


