"""adding a legend"""

import numpy as np
import matplotlib.pyplot as plt

def plot1():
    """plot1"""
    X = np.linspace(0, 6, 1024)
    Y1 = np.sin(X)
    Y2 = np.cos(X)

    plt.xlabel('X')
    plt.ylabel('Y')

    plt.plot(X, Y1, c='k', lw=3., label='sin(X)')
    plt.plot(X, Y2, c='.5', lw=3., ls='--', label='cos(X)')
    # legend is auto generated from the labels
    # loc => upper left; lower left; lower right; right;
    #        center left; center right; lower center;
    #        upper center; center;
    # shadow => True/False
    plt.legend()
    plt.show()

plot1()
