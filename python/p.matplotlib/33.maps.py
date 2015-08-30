#! coding: utf-8
'''working with maps'''

import numpy as np
import sympy
from sympy.abc import x, y
from numpy.random import uniform, seed
from matplotlib import cm as cm
from matplotlib import pyplot as plt
from matplotlib.mlab import griddata
from matplotlib import patches as patches


def iter_count(C, max_iter):
    '''iter_count'''
    X = C
    for n in range(max_iter):
        if abs(X) > 2.:
            return n
        X = X ** 2 + C
    return max_iter

def plot1():
    '''visualizing the content of a 2d array'''
    # reducing N will reduce the amount of computations
    N = 32
    # N = 512
    # N = 1024
    max_iter = 64
    xmin, xmax, ymin, ymax = -2.2, .8, -1.5, 1.5
    X = np.linspace(xmin, xmax, N)
    Y = np.linspace(ymin, ymax, N)
    Z = np.empty((N, N))

    for i, y in enumerate(Y):
        for j, x in enumerate(X):
            Z[i, j] = iter_count(complex(x, y), max_iter)

    # mandelbrot set
    # plt.imshow(Z, cmap=cm.gray)
    # plt.imshow(Z, cmap=cm.binary, extent=(xmin, xmax, ymin, ymax))
    # plt.imshow(Z, cmap=cm.binary, interpolation='nearest', \
    plt.imshow(Z, cmap=cm.binary, interpolation='bicubic', \
        extent=(xmin, xmax, ymin, ymax))
    plt.show()

def plot2():
    '''adding a colormap legend to a figure'''
    N = 32
    max_iter = 64
    xmin, xmax, ymin, ymax = -2.2, .8, -1.5, 1.5
    X = np.linspace(xmin, xmax, N)
    Y = np.linspace(ymin, ymax, N)
    Z = np.empty((N, N))

    for i, y in enumerate(Y):
        for j, x in enumerate(X):
            Z[i, j] = iter_count(complex(x, y), max_iter)

    # mandelbrot set
    plt.imshow(Z, cmap=cm.binary, interpolation='bicubic', \
        extent=(xmin, xmax, ymin, ymax))
    # colorbar
    cb = plt.colorbar(orientation='horizontal', shrink=.75)
    cb.set_label('iteration count')
    plt.show()

def plot3():
    '''visualizing nonuniform 2d data'''
    max_iter = 64
    xmin, xmax, ymin, ymax = -2.2, .8, -1.5, 1.5

    # randomly samples the mandelbrot set
    sample_count = 2 ** 12
    # array a and b hold the coordinates of the samples
    A = uniform(xmin, xmax, sample_count)
    B = uniform(ymin, ymax, sample_count)
    # c contains the value for each of these samples
    C = [iter_count(complex(a, b), max_iter) for a, b in zip(A, B)]

    # produce a 2d array of data
    # from the nonuniform samples
    N = 512
    # array `x` and `y` define a regular grid
    X = np.linspace(xmin, xmax, N)
    Y = np.linspace(ymin, ymax, N)
    # array `z` is a 2d array
    # built by interpolating the nonuniform samples
    Z = griddata(A, B, C, X, Y, interp='linear')

    plt.scatter(A, B, color=(0., 0., 0., .5), s=.5)
    plt.imshow(Z, cmap=cm.binary, 
               interpolation='bicubic',
               extent=(xmin, xmax, ymin, ymax))
    plt.show()

def plot4():
    '''visualizing a 2d scatter field'''
    n = 256
    x = np.linspace(-3., 3., n)
    y = np.linspace(-3., 3., n)
    X, Y = np.meshgrid(x, y)

    Z = X * np.sinc(X ** 2 + Y ** 2)

    plt.pcolormesh(X, Y, Z, cmap=cm.gray)
    plt.show()

def plot5():
    '''visualizing contour lines'''
    N = 512
    max_iter = 64
    # zoom inside a particular detail
    # of the mandelbrot set
    xmin, xmax, ymin, ymax = -0.32, -0.22, 0.8, 0.9
    X = np.linspace(xmin, xmax, N)
    Y = np.linspace(ymin, ymax, N)
    Z = np.empty((N, N))

    for i, y in enumerate(Y):
        for j, x in enumerate(X):
            Z[i, j] = iter_count(complex(x, y), max_iter)

    plt.imshow(Z,
               cmap=cm.binary,
               interpolation='bicubic',
               origin='lower',
               extent=(xmin, xmax, ymin, ymax))
    # show detail of the mandelbrot set
    # with sophisticated contour annotations
    levels = [8, 12, 16, 20]
    ct = plt.contour(X, Y, Z, levels, cmap=cm.gray)
    plt.clabel(ct, fmt='%d')
    plt.show()

def plot6():
    '''visualizing contour lines'''
    N = 512
    max_iter = 64
    # zoom inside a particular detail
    # of the mandelbrot set
    xmin, xmax, ymin, ymax = -0.32, -0.22, 0.8, 0.9
    X = np.linspace(xmin, xmax, N)
    Y = np.linspace(ymin, ymax, N)
    Z = np.empty((N, N))

    for i, y in enumerate(Y):
        for j, x in enumerate(X):
            Z[i, j] = iter_count(complex(x, y), max_iter)

    plt.imshow(Z,
               cmap=cm.binary,
               interpolation='bicubic',
               origin='lower',
               extent=(xmin, xmax, ymin, ymax))
    # show detail of the mandelbrot set
    # with sophisticated contour annotations
    levels = [0, 8, 12, 16, 20, 24, 32]
    plt.contourf(X, Y, Z, levels, cmap=cm.gray, antialiased=True)
    plt.show()

def cylinder_stream_funcion(U=1, R=1):
    '''cylinder_stream_funcion'''
    r = sympy.sqrt(x ** 2 + y ** 2)
    theta = sympy.atan2(y, x)
    return U * (r - R ** 2 / r) * sympy.sin(theta)

def velocity_field(psi):
    '''velocity_field'''
    u = sympy.lambdify((x, y), psi.diff(y), 'numpy')
    v = sympy.lambdify((x, y), -psi.diff(x), 'numpy')
    return u, v

def plot7():
    '''visualizing a 2d vector field'''
    U_func, V_func = velocity_field(cylinder_stream_funcion())

    xmin, xmax, ymin, ymax = -2.5, 2.5, -2.5, 2.5
    Y, X = np.ogrid[ymin:ymax:16j, xmin:xmax:16j]
    U, V = U_func(X, Y), V_func(X, Y)

    M = (X ** 2 + Y ** 2) < 1.
    U = np.ma.masked_array(U, mask=M)
    V = np.ma.masked_array(V, mask=M)

    shape = patches.Circle((0, 0), radius=1., lw=2., fc='w', ec='k', zorder=0)
    plt.gca().add_patch(shape)

    plt.quiver(X, Y, U, V, zorder=1)
    plt.axes().set_aspect('equal')
    plt.show()

def plot8():
    '''visualizing the streamlines of a 2d vector field'''
    psi = cylinder_stream_funcion()
    U_func, V_func = velocity_field(psi)

    xmin, xmax, ymin, ymax = -3, 3, -3, 3
    # more samples to get accurate streamlines
    Y, X = np.ogrid[ymin:ymax:128j, xmin:xmax:128j]
    U, V = U_func(X, Y), V_func(X, Y)

    M = (X ** 2 + Y ** 2) < 1.
    U = np.ma.masked_array(U, mask=M)
    V = np.ma.masked_array(V, mask=M)

    shape = patches.Circle((0, 0), radius=1., lw=2., fc='w', ec='k', zorder=0)
    plt.gca().add_patch(shape)

    # plt.streamplot(X, Y, U, V, color='k')
    plt.streamplot(X, Y, U, V, color=U ** 2 + V ** 2, cmap=cm.binary)
    plt.axes().set_aspect('equal')
    plt.show()

plot8()
