"""plotting points"""

import numpy as np
import matplotlib.pyplot as plt

def plot1():
	data = np.random.rand(1024, 2)
	plt.scatter(data[:,0], data[:,1])
	plt.show()

plot1()
