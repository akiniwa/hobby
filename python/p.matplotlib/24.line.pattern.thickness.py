"""controlling a line pattern and thickness"""

import numpy as np
import matplotlib.pyplot as plt

def pdf(X, mu, sigma):
    """pdf"""
    a = 1. / (sigma * np.sqrt(2. * np.pi))
    b = -1. / (2. * sigma ** 2)
    return a * np.exp(b * (X -mu) ** 2)

def plot1():
    """plot1"""
    X = np.linspace(-6, 6, 1024)

    plt.plot(X, pdf(X, 0., 1.0), color='b', linestyle='solid')
    plt.plot(X, pdf(X, 0., .75), color='g', linestyle='dashed')
    plt.plot(X, pdf(X, 0., .50), color='r', linestyle='dashdot')
    plt.plot(X, pdf(X, 0., .25), color='k', linestyle='dotted')
    plt.show()

def plot2():
    """plot2"""
    N = 8
    A = np.random.random(N)
    B = np.random.random(N)
    X = np.arange(N)

    plt.bar(X, A, color='g')
    plt.bar(X, A + B, bottom=A, color='w', linestyle='dashed')
    plt.show()

def plot3():
    """plot3"""
    X = np.linspace(-6, 6, 1024)
    for i in range(64):
        samples = np.random.standard_normal(50)
        mu, sigma = np.mean(samples), np.std(samples)
        plt.plot(X, pdf(X, mu, sigma), color='.75', linewidth=.5)
    plt.plot(X, pdf(X, 0., 1.), color='y', linewidth=3.)
    plt.show()

def plot4():
    """plot4"""
    N = 8
    A = np.random.random(N)
    B = np.random.random(N)
    X = np.arange(N)
    # / \ | - + x o O . *
    plt.bar(X, A, color='w', hatch='+')
    plt.bar(X, A + B, bottom=A, color='w', hatch='*')
    plt.show()

def plot5():
    """plot5"""
    A = np.random.standard_normal((100, 2))
    A += np.array((-1, -1))
    B = np.random.standard_normal((100, 2))
    B += np.array((1, 1))
    plt.scatter(A[:, 0], A[:, 1], color='k', marker='x')
    plt.scatter(B[:, 0], B[:, 1], color='k', marker='^')
    plt.show()

# plot1()
# plot2()
# plot3()
# plot4()
plot5()
