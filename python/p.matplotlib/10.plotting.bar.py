"""plotting bar"""

import numpy as np
import matplotlib.pyplot as plt

data = [5., 25., 50., 20.]

def plot1():
    """plot1"""
    plt.bar(range(len(data)), data)
    plt.show()

def plot2():
    """thickness of a bar"""
    plt.bar(range(len(data)), data, width=1.)
    plt.show()

def plot3():
    """plot3"""
    plt.barh(range(len(data)), data)
    plt.show()

def plot4():
    """multiple bar charts"""
    data = [[5, 25, 50, 20],
            [4, 23, 51, 17],
            [6, 22, 52, 19]]
    X = np.arange(4)
    plt.bar(X + 0.00, data[0], color='r', width=.25)
    plt.bar(X + 0.25, data[1], color='g', width=.25)
    plt.bar(X + 0.50, data[2], color='b', width=.25)
    plt.show()

def plot5():
    """multiple bar charts"""
    data = [[5, 25, 50, 20],
            [4, 23, 51, 17],
            [7, 21, 49, 21],
            [6, 22, 52, 19]]

    color_list = ['r', 'g', 'b']
    gap = .8 / len(data)

    for i, row in enumerate(data):
        X = np.arange(len(row))
        plt.bar(X + i * gap, row, width=gap, color=color_list[i % len(color_list)])
    plt.show()

def plot6():
    """stacked bar charts"""
    A = [5, 30, 45, 22]
    B = [5, 25, 50, 20]

    X = range(4)

    plt.bar(X, A, color='b')
    plt.bar(X, B, color='r', bottom=A)
    plt.show()

def plot7():
    """stacked bar charts"""
    A = np.array([5, 30, 45, 22])
    B = np.array([5, 25, 50, 20])
    C = np.array([1, 2, 1, 1])

    X = np.arange(4)

    plt.bar(X, A, color='b')
    plt.bar(X, B, color='g', bottom=A)
    plt.bar(X, C, color='r', bottom=A+B)
    plt.show()

def plot8():
    """back-to-back bar charts"""
    women = np.array([5, 30, 45, 22])
    men = np.array([5, 25, 50, 20])

    X = np.arange(4)

    plt.barh(X, women, color='r')
    plt.barh(X, -men, color='b')
    plt.show()

# plot1()
# plot2()
# plot3()
# plot4()
# plot5()
# plot6()
# plot7()
plot8()
