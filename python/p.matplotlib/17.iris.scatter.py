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

def load(data=1):
    """loadtxt from 1 => 17.bezdekIris.data else 17.iris.data"""
    filename = '17.bezdekIris.data' if 1 == data else '17.iris.data'
    return np.loadtxt(filename, delimiter=',', converters={4: read_label})

def plot1():
    """plot1"""
    data = load(1)
    color_set = ('.00', '.50', '.75')
    color_list = [color_set[int(label)] for label in data[:, 4]]
    plt.scatter(data[:, 0], data[:, 1], color=color_list)
    plt.show()

def plot2():
    """plot2"""
    data = load(0)
    marker_set = ('^', 'x', '.')
    color_set = ['r', 'g', 'b']
    for i, marker in enumerate(marker_set):
        data_subset = np.asarray([x for x in data if x[4] == i])
        plt.scatter(data_subset[:, 0], data_subset[:, 1], color=color_set[i], marker=marker)
    plt.show()

# plot1()
plot2()
