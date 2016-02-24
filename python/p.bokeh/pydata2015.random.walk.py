#! coding: utf-8

import collections
import datetime
import time

import numpy as np

from bokeh.io import curdoc
from bokeh.client import push_session
from bokeh.plotting import figure, show


# *To run these examples you must execute the command
# `bokeh serve` in the top-level Bokeh source directory first.*

TS_MULT_us = 1e6
# offset-naive datetime
UNIX_EPOCH = datetime.datetime(1970, 1, 1, 0, 0)


def int2dt(ts, ts_mult=TS_MULT_us):
    """Convert timestamp (integer) to datetime"""
    return(datetime.datetime.utcfromtimestamp(float(ts)/ts_mult))


def td2int(td, ts_mult=TS_MULT_us):
    """Convert timedelta to integer"""
    return(int(td.total_seconds()*ts_mult))


def dt2int(dt, ts_mult=TS_MULT_us):
    """Convert datetime to integer"""
    delta = dt - UNIX_EPOCH
    return(int(delta.total_seconds()*ts_mult))


def int_from_last_sample(dt, td):
    return(dt2int(dt) - dt2int(dt) % td2int(td))


TS_MULT = 1e3
td_delay = datetime.timedelta(seconds=0.5)
delay_s = td_delay.total_seconds()
delay_int = td2int(td_delay, TS_MULT)

# initial value
value = 1000
# number of elements into circular buffer
N = 100

buff = collections.deque([value]*N, maxlen=N)


t_now = datetime.datetime.utcnow()
ts_now = dt2int(t_now, TS_MULT)
t = collections.deque(np.arange(ts_now-N*delay_int, ts_now, delay_int), maxlen=N)

p = figure(x_axis_type="datetime")
p.line(list(t), list(buff), color="#0000FF", name="line_example")

renderer = p.select(dict(name="line_example"))[0]
ds = renderer.data_source


def update():
    ts_now = dt2int(datetime.datetime.utcnow(), 1e3)
    t.append(ts_now)
    ds.data['x'] = list(t)

    global value
    value += np.random.uniform(-1, 1)
    buff.append(value)
    ds.data['y'] = list(buff)

# run every 50 milliseconds
curdoc().add_periodic_callback(update, delay_s * 100)

session = push_session(curdoc())
# open the doc in browser
session.show()

# run forever
session.loop_until_closed()
