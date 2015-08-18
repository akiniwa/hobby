"""show curve Y =X ** 2 with x in [0, 99]"""

import matplotlib.pyplot as plt

X = range(100)
Y = [value ** 2 for value in X]
plt.plot(X, Y)
plt.show()
