#! coding: utf-8

import time
import datetime

tss = [
    1454290307000,
    1454290264000,
    1454290223000,
    1454290180000,
    1454290139000,
    1454290095000,
    1454290052000,
    1454290009000,
    1454289968000,
    1454289925000,
]


def ts_to_date(ts):
    '''ts_to_date'''
    ct = time.ctime(ts / 1000.0)
    dt = datetime.datetime.strptime(ct, '%a %b %d %H:%M:%S %Y')
    return dt.strftime('%Y-%m-%d %H:%M:%S')


if __name__ == '__main__':
    print '\n'.join([ts_to_date(ts) for ts in tss])
