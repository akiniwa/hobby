"""marker"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.path as mpath

def plot1():
    """plot1"""
    X = np.linspace(-6, 6, 1024)
    Y1 = np.sinc(X)
    Y2 = np.sinc(X) + 1

    plt.plot(X, Y1, marker='*', color='b', markevery=32)
    plt.plot(X, Y2, marker='^', color='r', markevery=32)
    plt.show()

def plot2():
    """controlling a marker's size"""
    A = np.random.standard_normal((100, 2))
    A += np.array((-1, -1))
    B = np.random.standard_normal((100, 2))
    B += np.array((1, 1))
    plt.scatter(A[:, 0], A[:, 1], c='w', s=25.)
    plt.scatter(B[:, 0], B[:, 1], c='k', s=50.)
    plt.show()

def plot3():
    """plot3"""
    M = np.random.standard_normal((1000, 2))
    R = np.sum(M ** 2, axis=1)

    plt.scatter(M[:, 0], M[:, 1], c='w', marker='s', s=32. * R)
    plt.show()

def plot4():
    """create your own marker"""
    shape_description = [
        (1., 2., mpath.Path.MOVETO),
        (1., 1., mpath.Path.LINETO),
        (2., 1., mpath.Path.LINETO),
        (2., -1., mpath.Path.LINETO),
        (1., -1., mpath.Path.LINETO),
        (1., -2., mpath.Path.LINETO),
        (-1., -2., mpath.Path.LINETO),
        (-1., -1., mpath.Path.LINETO),
        (-2., -1., mpath.Path.LINETO),
        (-2., 1., mpath.Path.LINETO),
        (-1., 1., mpath.Path.LINETO),
        (-1., 2., mpath.Path.LINETO),
        (0., 0., mpath.Path.CLOSEPOLY),
    ]
    u, v, codes = zip(*shape_description)
    my_marker = mpath.Path(np.asarray((u, v)).T, codes)
    data = np.random.rand(8, 8)
    plt.scatter(data[:, 0], data[:, 1], c='.75', marker=my_marker, s=64)
    plt.show()

def plot5():
    """more control over markers"""
    X = np.linspace(-6, 6, 1024)
    Y = np.sinc(X)

    plt.plot(X, Y,
        linewidth=3.,
        color='k',
        markersize=9,
        markeredgewidth=1.5,
        markerfacecolor='.75',
        marker='*',
        markevery=32)
    plt.show()

def plot6():
    """creating your own color scheme"""
    mpl.rc('lines', linewidth=2.)
    mpl.rc('axes', facecolor='k', edgecolor='w')
    mpl.rc('ytick', color='w')
    mpl.rc('xtick', color='w')
    mpl.rc('text', color='w')
    mpl.rc('figure', facecolor='k', edgecolor='w')
    mpl.rc('axes', color_cycle=('w', '.5', '.75'))
    X = np.linspace(0, 7, 1024)
    plt.plot(X, np.sin(X))
    plt.plot(X, np.cos(X))
    plt.show()

# plot1()
# plot2()
# plot3()
# plot4()
# plot5()
plot6()
