"""plotting triangulations"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as tri

def plot1():
	"""plot1"""
	data = np.random.rand(100, 2)
	triangles = tri.Triangulation(data[:,0], data[:,1])
	plt.triplot(triangles)
	plt.show()

plot1()
