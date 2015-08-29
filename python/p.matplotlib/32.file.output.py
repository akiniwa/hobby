#! coding: utf-8
'''working with a file output'''

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def plot1():
    '''generating a png file'''
    X = np.linspace(-10, 10, 1024)
    Y = np.sinc(X)

    plt.plot(X, Y)
    # resolution 800 x 600
    # 8-bit colors (24-bits per pixel)
    plt.savefig('32.sinc.png', c='k')

def plot2():
    '''handing transparency'''
    X = np.linspace(-10, 10, 1024)
    Y = np.sinc(X)

    plt.plot(X, Y, c='k')
    plt.savefig('32.sinc.transparent.png', transparent=True)

def plot3():
    '''content transparency'''
    name_list = ('omar', 'serguey', 'max', 'zhou', 'abidin')
    value_list = np.random.randint(99, size=len(name_list))
    post_list = np.arange(len(name_list))

    plt.bar(post_list, value_list, alpha=.75, color='.75', align='center')
    plt.xticks(post_list, name_list)

    plt.savefig('32.bar.png', transparent=True)

def plot4():
    '''controlling the output resolution'''
    X = np.linspace(-10, 10, 1024)
    Y = np.sinc(X)

    plt.plot(X, Y)
    # by default matplotlib will output
    # 8 x 6 spatial units a 4/3 aspect ratio
    # in matplotlib 1 spatial unit equals to 100 pixels
    # by default 800 x 600 pixels
    # if dpi = 300 picture size will be
    # 8 * 300 x 6 * 300 => 2400 x 1800
    plt.savefig('32.sinc.dpi.png', dpi=300)

def plot5():
    '''display a hexagon in 512 x 512 pixels'''
    theta = np.linspace(0, 2 * np.pi, 8)
    points = np.vstack((np.cos(theta), np.sin(theta))).transpose()

    # 4 * 128 x 4 * 128 => 512 x 512
    plt.figure(figsize=(4., 4.))
    plt.gca().add_patch(plt.Polygon(points, color='.75'))

    plt.grid(True)
    plt.axis('scaled')

    plt.savefig('32.polygon.png', dpi=128)

def plot6():
    '''generating pdf or svg documents'''
    X = np.linspace(-10, 10, 1024)
    Y = np.sinc(X)

    plt.plot(X, Y)
    # plt.savefig('32.sinc.pdf')
    plt.savefig('32.sinc.svg')

def plot7():
    '''handing multiple-page pdf documents'''
    # generate data
    data = np.random.randn(15, 1024)
    # the pdf document
    pdf_pages = PdfPages('32.barcharts.pdf')
    # generate the pages
    plots_counts = data.shape[0]
    plots_per_page = 5
    pages_count = int(np.ceil(plots_counts / float(plots_per_page)))
    grid_size = (plots_per_page, 1)

    for i, samples in enumerate(data):
        # create a figure instance ie. a new page if needed
        if 0 == i % plots_per_page:
            fig = plt.figure(figsize=(8.27, 11.69), dpi=100)

        # plot one bar chart
        plt.subplot2grid(grid_size, (i % plots_per_page, 0))
        plt.hist(samples, 32, normed=1, facecolor='.5', alpha=0.75)

        # close the page if needed
        if 0 == (i + 1) % plots_per_page or plots_counts == (i + 1):
            plt.tight_layout()
            pdf_pages.savefig(fig)

    # write the pdf document to disk
    pdf_pages.close()

plot7()
