"""adding shapes"""

import matplotlib.patches as patches
import matplotlib.pyplot as plt

def plot1():
    """plot1"""
    shape = patches.Circle((0, 0), radius=1, color='.75')
    plt.gca().add_patch(shape)

    shape = patches.Rectangle((2.5, -.5), 2., 1., color='.75')
    plt.gca().add_patch(shape)

    shape = patches.Ellipse((0, -2.), 2., 1., angle=45., color='.75')
    plt.gca().add_patch(shape)
    
    # boxstyle => larrow; rarrow; round; round4; roundtooth; sawtooth; square
    shape = patches.FancyBboxPatch((2.5, -2.5), 2., 1., boxstyle='roundtooth', color='.75')
    plt.gca().add_patch(shape)

    plt.grid(True)
    plt.axis('scaled')
    plt.show()

plot1()
