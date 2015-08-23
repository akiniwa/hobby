"""adding lines"""

import matplotlib.pyplot as plt

def plot1():
	"""plot1"""
	N = 64
	for i in range(N):
		plt.gca().add_line(plt.Line2D((0, i), (N - i, 0), color='.75'))

	plt.grid(True)
	plt.axis('scaled')
	plt.show()

plot1()
