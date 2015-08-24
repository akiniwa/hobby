"""adding shapes"""

import numpy as np
import datetime
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def plot1():
    """plot1"""
    shape = patches.Circle((0, 0), radius=1, color='.75')
    plt.gca().add_patch(shape)

    shape = patches.Rectangle((2.5, -.5), 2., 1., color='.75')
    plt.gca().add_patch(shape)

    shape = patches.Ellipse((0, -2.), 2., 1., angle=45., color='.75')
    plt.gca().add_patch(shape)

    # boxstyle => larrow; rarrow; round; round4; roundtooth; sawtooth; square
    shape = patches.FancyBboxPatch((2.5, -2.5), 2., 1., boxstyle='roundtooth', color='.75')
    plt.gca().add_patch(shape)

    plt.grid(True)
    plt.axis('scaled')
    plt.show()

def plot2():
    """working with polygons"""
    # theta = np.linspace(0, 2 * np.pi, 8)
    theta = np.linspace(0, 2 * np.pi, 9)
    # theta = np.linspace(0, 2 * np.pi, 10)
    # points = np.vstack((np.cos(theta), np.sin(theta))).transpose()
    points = np.vstack((np.sin(theta), np.cos(theta))).transpose()

    plt.gca().add_patch(patches.Polygon(points, color='.75'))
    plt.grid(True)
    plt.axis('scaled')
    plt.show()

def plot3():
    """working with path attributes"""
    theta = np.linspace(0, 2 * np.pi, 6)
    points = np.vstack((np.sin(theta), np.cos(theta))).transpose()
    plt.gca().add_patch(plt.Circle((0, 0), radius=1., color='.75'))
    plt.gca().add_patch(plt.Polygon(points, closed=None, fill=None, lw=3., ls='dashed', edgecolor='k'))
    plt.grid(True)
    plt.axis('scaled')
    plt.show()

def plot4():
    """controlling tick spacing"""
    X = np.linspace(-15, 15, 1024)
    Y = np.sinc(X)

    ax = plt.axes()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))

    plt.grid(True, which='both')
    plt.plot(X, Y, c='k')
    plt.show()

def plot5():
    """controlling tick labeling"""
    name_list = ('omar', 'serguey', 'max', 'zhou', 'abidin')
    value_list = np.random.randint(0, 99, size=len(name_list))
    pos_list = np.arange(len(name_list))

    ax = plt.axes()
    ax.xaxis.set_major_locator(ticker.FixedLocator((pos_list)))
    ax.xaxis.set_major_formatter(ticker.FixedFormatter(name_list))

    plt.bar(pos_list, value_list, color='.75', align='center')
    plt.show()

def plot6():
    """simpler way to create bar charts with fixed labels"""
    name_list = ('omar', 'serguey', 'max', 'zhou', 'abidin')
    value_list = np.random.randint(0, 99, size=len(name_list))
    pos_list = np.arange(len(name_list))

    plt.bar(pos_list, value_list, color='.75', align='center')
    plt.xticks(pos_list, name_list)
    plt.show()

def make_label7(value, pos):
    """make_label7"""
    return '%0.1f%%' % (100. * value)

def plot7():
    """advanced label generation"""
    ax = plt.axes()
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(make_label7))
    X = np.linspace(0, 1, 256)
    plt.plot(X, np.exp(-10 * X), c='k')
    plt.plot(X, np.exp(-5 * X), c='k', ls='--')
    plt.show()

start_date = datetime.datetime(1998, 1, 1)

def make_lable8(value, pos):
    """make_lable8"""
    time = start_date + datetime.timedelta(days=356 * value)
    return time.strftime('%b %y')

def plot8():
    """delegation"""
    ax = plt.axes()
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(make_lable8))
    X = np.linspace(0, 1, 256)
    plt.plot(X, np.exp(-10 * X), c='k')
    plt.plot(X, np.exp(-5 * X), c='k', ls='--')
    labels = ax.get_xticklabels()
    plt.setp(labels, rotation=30.)
    plt.show()

# plot1()
# plot2()
# plot3()
# plot4()
# plot5()
# plot6()
# plot7()
plot8()
