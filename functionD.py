#Name:Cihat Bostancı
#ID : 150160542
import matplotlib.pyplot as plt
import numpy as np
import sys

def functionC(x1, y1,sliceData):



    y = []
    for i in range(0, len(x1)):
        y.append(0)
        for j in range(0, len(y1)):

            y[i] += x1[i - j] * y1[j];


    markerline, stemlines, baseline = plt.stem(sliceData ,np.array(y), '-.')
    plt.setp(baseline, 'color', 'r', 'linewidth', 4)
    plt.ylabel("y[n]")
    plt.xlabel("[n]")
    plt.show()

def Mean(Signal):
    return sum(Signal)/len(Signal)

def StandardDeviation(Signal):
    mean = Mean(Signal)
    var = sum((x-mean)*(x-mean) for x in Signal) / len(Signal)  # variance
    std = var**0.5
    return std

def functionB(data,data2,data3,data4):

    mean1 = Mean(data)
    mean2 = Mean(data3)
    data_norm_to_1 = [(number - mean1) / StandardDeviation(data) for number in data]
    data_norm_to_2 = [(number1 - mean2) / StandardDeviation(data3) for number1 in data3]

    functionC(data_norm_to_1, data_norm_to_2, data2)




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

    functionB(xnp, xSlicenp, y, ySlicenp)


