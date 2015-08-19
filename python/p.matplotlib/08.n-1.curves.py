"""n columns data n - 1 curves"""

import numpy as np
import matplotlib.pyplot as plt

def plot1():
	"""plot"""
	data = np.loadtxt('08.txt')
	for column in data.T:
		plt.plot(data[:, 0], column)

	plt.show()

plot1()
