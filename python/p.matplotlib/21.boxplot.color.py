"""custom color for boxplots"""

import numpy as np
import matplotlib.pyplot as plt

def plot1():
	"""plot1"""
	values = np.random.randn(100)
	b = plt.boxplot(values)

	for name, line_list in b.iteritems():
		for line in line_list:
			line.set_color('r')

	plt.show()

plot1()
