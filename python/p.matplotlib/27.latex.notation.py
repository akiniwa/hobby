"""latex-style notations"""

import numpy as np
import matplotlib.pyplot as plt

def plot1():
    """using latex-style notations"""
    X = np.linspace(-4, 4, 1024)
    Y = .25 * (X + 4.) * (X + 1.) * (X - 2.)

    plt.title('$f(X)=\\frac{1}{4}(x+4)(x+1)(x-2)$')
    plt.plot(X, Y, c='k')
    plt.show()

def plot2():
    """adding a label to each axis"""
    X = np.linspace(-4, 4, 1024)
    Y = .25 * (X + 4.) * (X + 1.) * (X - 2.)

    plt.title('power curve for airfoil kv873')
    plt.xlabel('air speed')
    plt.ylabel('total drag')
    plt.plot(X, Y, c='k')
    plt.show()

def plot3():
    """adding text"""
    X = np.linspace(-4, 4, 1024)
    Y = .25 * (X + 4.) * (X + 1.) * (X - 2.)

    plt.text(-0.5, -0.25, 'brackmark minimum')
    # verticalalignment   center top bottom baseline
    # horizontalalignment right left center
    plt.plot(X, Y, c='k')
    plt.show()

def plot4():
    """bounding box control"""
    X = np.linspace(-4, 4, 1024)
    Y = .25 * (X + 4.) * (X + 1.) * (X - 2.)

    box = {
        'facecolor' : '.75',
        'edgecolor' : 'k',
        'boxstyle' : 'round',
    }

    plt.text(-0.5, -0.25, 'brackmark minimum', bbox=box, verticalalignment='baseline')
    plt.plot(X, Y, c='k')
    plt.show()

def plot5():
    """adding arrows"""
    X = np.linspace(-4, 4, 1024)
    Y = .25 * (X + 4.) * (X + 1.) * (X - 2.)

    plt.annotate('brackmark minimum', \
        ha='center', va='bottom', \
        xytext=(-1.5, 3.), \
        xy=(0.75, -2.7), \
        arrowprops={'facecolor' : 'black', 'shrink' : 0.05})
    # arrowstyle simple/fancy/wedge/->/<-/<->
    plt.plot(X, Y)
    plt.show()

def plot6():
    """adding grid"""
    X = np.linspace(-4, 4, 1024)
    Y = .25 * (X + 4.) * (X + 1.) * (X - 2.)

    plt.text(-0.5, -0.25, 'brackmark minimum')
    plt.plot(X, Y, c='k')
    plt.grid(True, lw=2, ls='--', c='.75')
    plt.show()

# plot1()
# plot2()
# plot3()
# plot4()
# plot5()
plot6()
