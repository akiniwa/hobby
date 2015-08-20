"""defining your own colors"""

"""
1. triplets
2. quadruplets
3. predefined names
	b blue
	g green
	r red
	c cyan
	m magenta
	y yellow
	k black
	w white
4. html color strings
5. gray-level strings
"""

import numpy as np
import matplotlib.pyplot as plt

def pdf(X, mu, sigma):
	"""pdf"""
	a = 1. / (sigma * np.sqrt(2. * np.pi))
	b = -1. / (2. * sigma ** 2)
	return a * np.exp(b * (X - mu) ** 2)

def plot1():
	"""plot1"""
	X = np.linspace(-6, 6, 1000)

	for i in range(5):
		samples = np.random.standard_normal(50)
		mu, sigma = np.mean(samples), np.std(samples)
		plt.plot(X, pdf(X, mu, sigma), color='.75')

	plt.plot(X, pdf(X, 0., 1.), color='k')
	plt.show()

plot1()
