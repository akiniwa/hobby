"""custom colors for bar charts"""

import numpy as np
import matplotlib.pyplot as plt

def plot1():
    """plot1"""
    women = np.array([5., 30., 45., 22.])
    men = np.array([5., 25., 50., 20.])

    X = np.arange(4)
    plt.barh(X, women, color='.25')
    plt.barh(X, -men, color='.75')

    plt.show()

def plot2():
    """plot2"""
    # values = np.random.random_integers(99, size=50)
    values = sorted(np.random.random_integers(99, size=50))

    color_set = ('.00', '.25', '.50', '.75')
    color_list = [color_set[(len(color_set) * val) / 100] for val in values]
    plt.bar(np.arange(len(values)), values, color=color_list)
    plt.show()


# plot1()
plot2()
