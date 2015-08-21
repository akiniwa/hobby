"""edgecolor controls the color of the edge of the dots"""

import numpy as np
import matplotlib.pyplot as plt


def plot1():
    """plot1"""
    data = np.random.standard_normal((100, 2))
    plt.scatter(data[:, 0], data[:, 1], color='.9', edgecolor='.1')
    plt.show()

plot1()
