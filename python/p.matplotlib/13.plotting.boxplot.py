"""plotting boxplots"""

import numpy as np
import matplotlib.pyplot as plt

def plot1():
	"""plot1"""
	data = np.random.randn(100)
	plt.boxplot(data)
	plt.show()

def plot2():
	"""plot2"""
	data = np.random.randn(100, 5)
	plt.boxplot(data)
	plt.show()


# plot1()
plot2()
