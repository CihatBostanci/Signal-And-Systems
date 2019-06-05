#Name:Cihat Bostancı
#ID : 150160542
import matplotlib.pyplot as plt
import numpy as np
import sys

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

    f, (ax1, ax2) = plt.subplots(1, 2)

    markerline, stemlines, baseline = ax1.stem(data2, data_norm_to_1, '-.')
    plt.setp(baseline, 'color', 'r', 'linewidth', 3)
    plt.ylabel("y[n]")
    plt.xlabel("[n]")
    plt.title("Signal Sample")

    markerline, stemlines, baseline = ax2.stem(data4, data_norm_to_2, '-.')
    plt.setp(baseline, 'color', 'r', 'linewidth', 3)
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

    functionB(xnp, xSlicenp, y, ySlicenp)


