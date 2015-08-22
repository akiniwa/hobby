"""colormaps for scatter plots"""

import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt

def plot1():
	"""plot1"""
	N = 256
	angle = np.linspace(0, 8 * 2 * np.pi, N)
	radis = np.linspace(.5, 1., N)
	X = radis * np.cos(angle)
	Y = radis * np.sin(angle)
	plt.scatter(X, Y, c=angle, cmap=cm.hsv)
	plt.show()

plot1()
