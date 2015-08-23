"""adding a title"""

import numpy as np
import matplotlib.pyplot as plt

def plot1():
    """plot1"""
    X = np.linspace(-4, 4, 2014)
    Y = .25 * (X + 4.) * (X + 1.) * (X - 2.)

    plt.title("a polynomial")
    plt.plot(X, Y, c='k')
    plt.show()

plot1()
