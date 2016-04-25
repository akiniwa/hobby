#! *-* coding: utf-8 *-*
"""this is a demo docstring"""
import math


def minute_seg():
    data = {}
    for i in range(0, 1440):
        h = i / 60
        # m = i % 60
        m = 0
        d = "{}:{}-{}:{}".format(str(h).zfill(2),
                                 str(m).zfill(2),
                                 str(h+1).zfill(2),
                                 str(m).zfill(2))
        data[str(i)] = d

    print data


def minute_sum():
    data = {}
    for i in range(0, 1440):
        h = i / 60
        m = i % 60 / 10
        # print i, m
        d = "{}:{}0".format(str(h).zfill(2), m)
        data[str(i)] = d

    print data


# minute_seg()
minute_sum()
