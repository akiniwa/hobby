"""plotting histograms"""

import numpy as np
import matplotlib.pyplot as plt

def plot1():
	"""plot1"""
	X = np.random.randn(1000)
	plt.hist(X, bins=20)
	plt.show()

plot1()
