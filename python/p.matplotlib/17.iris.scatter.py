"""iris"""

import numpy as np
import matplotlib.pyplot as plt

LABELSET = (
    b'Iris-setosa',
    b'Iris-versicolor',
    b'Iris-virginica'
)

def read_label(lable):
    """read_label"""
    return LABELSET.index(lable)

def plot1():
    """plot1"""
    # data = np.loadtxt('17.iris.data', delimiter=',', converters={4: read_label})
    data = np.loadtxt('17.bezdekIris.data', delimiter=',', converters={4: read_label})

    color_set = ('.00', '.50', '.75')
    color_list = [color_set[int(label)] for label in data[:, 4]]
    plt.scatter(data[:, 0], data[:, 1], color=color_list)
    plt.show()

plot1()
