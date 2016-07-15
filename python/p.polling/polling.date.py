#! coding: utf-8

import datetime
import polling


def print_now():
    """print_now"""
    print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    # run print_now every step sec
    polling.poll(print_now, step=1, poll_forever=True)
