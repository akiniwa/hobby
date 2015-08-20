"""custom colors for scatter plots"""

import numpy as np
import matplotlib.pyplot as plt

def plot1():
	"""plot1"""
	A = np.random.standard_normal((100, 2))
	# center the distrib at <-1, -1>
	A += np.array((-1, -1))

	B = np.random.standard_normal((100, 2))
	# center the distrib at <1, 1>
	B += np.array((1, 1))

	plt.scatter(A[:,0], A[:,1], color='.25')
	plt.scatter(B[:,0], B[:,1], color='.75')
	plt.show()

plot1()
