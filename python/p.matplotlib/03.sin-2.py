"""curve sin(x) with x in [0, 2 * pi]"""

import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0, 2 * np.pi, 100)
Y = np.sin(X)

plt.plot(X, Y)
plt.show()

X = np.linspace(-3, 2, 200)
Y = X ** 2 - 2 * X +1

plt.plot(X, Y)
plt.show()
