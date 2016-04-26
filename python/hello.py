#! *-* coding: utf-8 *-*
"""this is a demo docstring"""
import math


def minute_seg(step):
    data = minute_sum(step, is_print=False)
    data_seg = {}
    for i in range(0, 1440 - step):
        data_seg[str(i)] = data[str(i)] + '-' + data[str(i+step)]
        print i, data_seg[str(i)]
    # print data_seg


def minute_sum(step, is_print):
    data = {}
    for i in range(0, 1440):
        h = i / 60
        m = i % 60
        m = m - m % step
        d = "{}:{}".format(str(h).zfill(2), str(m).zfill(2))
        if is_print:
            print i, d
        data[str(i)] = d
    return data

# minute_seg(3)
minute_sum(3, is_print=True)
