"""colormaps for bar charts"""

import numpy as np
import matplotlib.cm as cm
import matplotlib.colors as col
import matplotlib.pyplot as plt

def plot1():
    """plot1"""
    # values = np.random.random_integers(99, size=50)
    values = sorted(np.random.random_integers(99, size=50))
    cmap = cm.ScalarMappable(col.Normalize(0, 99), cm.binary)
    plt.bar(np.arange(len(values)), values, color=cmap.to_rgba(values))
    plt.show()

plot1()
