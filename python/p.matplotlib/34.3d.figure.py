#! coding: utf-8
'''working with 3d figures'''

import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.colors as col

a, b, c = 10., 28., 8. / 3.
# a, b, c = 28., 46.92, 4.

def lorenz_map(X, dt=1e-2):
    '''
    lorenz attractor was first studied by ed n. lorenz
    the system is most commonly expressed as
    3 coupled non-linear differential equations
    dx / dt = a * (y - x)
    dy / dt = x * (b - z) - y
    dz / dt = x * y - c * z
    a => prandtl number
    b => rayleigh number
    '''
    X_dt = np.array([a * (X[1] - X[0]),
                     X[0] * (b - X[2]) - X[1],
                     X[0] * X[1] - c * X[2]])
    return X + dt * X_dt

def plot1():
    '''scatter plot'''
    points = np.zeros((2000, 3))
    X = np.array([.1, .0, .0])
    for i in range(points.shape[0]):
        points[i], X = X, lorenz_map(X)

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ax.set_xlabel('x axis')
    ax.set_ylabel('y axis')
    ax.set_zlabel('z axis')
    ax.set_title('lorenz attractor a=%0.2f b=%0.2f c=%0.2f' % (a, b, c))

    # ax.scatter(points[:, 0], points[:, 1], points[:, 2], zdir='y', c='k')
    ax.scatter(points[:, 0], points[:, 1], points[:, 2],
               marker='.', edgecolor='.5', facecolor='.5')
    plt.show()

def plot2():
    '''creating 3d curve plots'''
    points = np.zeros((10000, 3))
    X = np.array([.1, .0, .0])
    for i in range(points.shape[0]):
        points[i], X = X, lorenz_map(X)

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(points[:, 0], points[:, 1], points[:, 2], c='k')
    plt.show()

def plot3():
    '''plotting a scalar field in 3d'''
    x = np.linspace(-3, 3, 256)
    y = np.linspace(-3, 3, 256)
    X, Y = np.meshgrid(x, y)
    Z = np.sinc(np.sqrt(X ** 2 + Y ** 2))

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    # ax.plot_surface(X, Y, Z, cmap=cm.gray)
    # ax.plot_surface(X, Y, Z, cmap=cm.binary, linewidth=0, antialiased=False)
    # ax.plot_surface(X, Y, Z, color='w')
    ax.plot_surface(X, Y, Z, cstride=8, rstride=8, color='w')
    plt.show()

def plot4():
    '''plotting a parametric 2d surface'''
    # generate torus mesh
    angle = np.linspace(0, 2 * np.pi, 32)
    theta, phi = np.meshgrid(angle, angle)
    r, R = .25, 1.
    X = (R + r * np.cos(phi)) * np.cos(theta)
    Y = (R + r * np.cos(phi)) * np.sin(theta)
    Z = r * np.sin(phi)

    # display the mesh
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_xlim3d(-1, 1)
    ax.set_ylim3d(-1, 1)
    # ax.set_zlim3d(-1, 1)
    ax.set_zlim3d(-.25, .25)
    # ax.plot_surface(X, Y, Z, color='w', rstride=1, cstride=1)
    ax.plot_wireframe(X, Y, Z, color='k', rstride=1, cstride=1)
    plt.show()

def plot5():
    '''embedding 2d figures in a 3d figures'''
    x = np.linspace(-3, 3, 256)
    y = np.linspace(-3, 3, 256)
    X, Y = np.meshgrid(x, y)
    Z = np.exp(-(X ** 2 + Y ** 2))
    u = np.exp(-(x ** 2))

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_zlim3d(0, 3)
    # zdir => determines on which plane the 2d plot will be drawn
    # zs   => determines the offset of the plane
    ax.plot(x, u, zs=3, zdir='y', lw=2, color='r')
    ax.plot(x, u, zs=-3, zdir='x', lw=2, color='g')
    ax.plot_surface(X, Y, Z, color='w')
    plt.show()

def plot6():
    '''plot6'''
    # data generation
    alpha = 1. / np.linspace(1, 8, 5)
    t = np.linspace(0, 5, 16)
    T, A = np.meshgrid(t, alpha)
    data = np.exp(-T * A)

    # plotting
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    cmap = cm.ScalarMappable(col.Normalize(0, len(alpha)), cm.gray)
    for i, row in enumerate(data):
        ax.bar(4 * t, row, zs=i, zdir='y', alpha=0.8, color=cmap.to_rgba(i))
    plt.show()

def plot7():
    '''creating a 3d bar plot'''
    # data generation
    alpha = np.linspace(1, 8, 5)
    t = np.linspace(0, 5, 16)
    T, A = np.meshgrid(t, alpha)
    data = np.exp(-T * (1. / A))

    # plotting
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    Xi = T.flatten()
    Yi = A.flatten()
    Zi = np.zeros(data.size)

    dx = .25 * np.ones(data.size)
    dy = .25 * np.ones(data.size)
    dz = data.flatten()

    ax.set_xlabel('t')
    ax.set_ylabel('alpha')
    ax.bar3d(Xi, Yi, Zi, dx, dy, dz, color='w')
    plt.show()

plot7()
