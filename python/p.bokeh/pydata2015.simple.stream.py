#! conding utf-8

import time
import numpy as np

from bokeh.io import curdoc
from bokeh.client import push_session
from bokeh.models import GlyphRenderer
from bokeh.plotting import figure, show

x = np.linspace(0, 4*np.pi, 200)
y = np.sin(x)

p = figure(title="Simple streaming example")
p.line(x, y, color="#2222aa", line_width=2)
ds = p.select({"type": GlyphRenderer})[0].data_source


def update():
    oldx = ds.data["x"]
    newx = np.hstack([oldx, [oldx[-1] + 4*np.pi/200]])
    ds.data["x"] = newx
    ds.data["y"] = np.sin(newx)

# run every 5 milliseconds
curdoc().add_periodic_callback(update, 5)

session = push_session(curdoc(), 'simple-stream')
# open the doc in browser
session.show()
# run forever
session.loop_until_closed()
