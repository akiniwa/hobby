#! coding: utf-8
"""getting start with bokeh"""

from bokeh.plotting import figure, output_file, output_notebook, show

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# output_file('lines.html', title='line plot example')
output_notebook('lines.html')

p = figure(title='simple line example', x_axis_label='x', y_axis_label='y')

p.line(x, y, legend="Temp.", line_width=2)

show(p)

from ipywidgets import interact
import numpy as np

from bokeh.io import push_notebook
from bokeh.plotting import figure, show, output_notebook

x = np.linspace(0, 2 * np.pi, 2000)
y = np.sin(x)

output_notebook()

p = figure(title='simple line example', plot_height=300, plot_width=600, y_range=(-5, 5))
r = p.line(x, y, color='#2222aa', line_width=3)

def update(f, w=1, A=1, phi=0):
    """update"""
    if f == 'sin': func = np.sin
    elif f == 'cos': func = np.cos
    elif f == 'tan': func = np.tan
    r.data_source.data['y'] = A * func(w * x + phi)
    push_notebook()

show(p)

interact(update, f=['sin', 'cos', 'tan'], w=(0, 100), A=(1,5), phi=(0, 20, 0.1))