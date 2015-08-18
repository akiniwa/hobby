"""plotting curves from file data"""

import numpy as np
import matplotlib.pyplot as plt

def method0():
    """method0"""
    X, Y = [], []
    for line in open('07.txt', 'r'):
        values = [float(s) for s in line.split()]
        X.append(values[0])
        Y.append(values[1])

    plt.plot(X, Y)
    plt.show()

def method1():
    """method1"""
    with open('07.txt', 'r') as f:
        X, Y = zip(*[[float(s) for s in line.split()] for line in f])

    plt.plot(X, Y)
    plt.show()

def method2():
    """method2"""
    data = np.loadtxt('07.txt')
    plt.plot(data[:, 0], data[:, 1])
    plt.show()

method0()
# method1()
# method2()
