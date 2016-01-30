#! coding: utf-8
"""gen hbase demo data"""

import StringIO

# create 'test', 'cf'
# list 'test'
# put 'test', 'row1', 'cf:a', 'value1'
# put 'test', 'row2', 'cf:b', 'value2'
# put 'test', 'row3', 'cf:c', 'value3'
# put 'test', 'row4', 'cf:d', 'value4'
# scan 'test'
# get 'test', 'row1'
# disable 'test'
# enable 'test'

data_file = 'hbase.dat'

SIO = StringIO.StringIO()
DATE = '20160124'

SIO.write("disable 'test'")
SIO.write("\n")
SIO.write("drop 'test'")
SIO.write("\n")
SIO.write("create 'test', 'cf'")
SIO.write("\n")


def gen_all():
    """gen_all"""

    for indicator in range(0, 13):
        for store in range(0, 20001):
            for minute in range(1, 1441):
                # put 'test', '201601240000101', 'cf:0001', '0001'
                put = "put 'test', '{}{}{}', 'cf:{}', '{}'"\
                    .format(
                        DATE, (str(store)).zfill(5), (str(indicator)).zfill(2),
                        (str(minute)).zfill(4), (str(minute)).zfill(4)
                    )
                SIO.write(put)
                SIO.write('\n')
    with open(data_file, 'wt') as file_o:
        file_o.write(SIO.getvalue())


def gen_one():
    """gen_one"""

    indicator = 0
    for store in range(10000, 10001):
        for minute in range(1, 1441):
            # put 'test', '201601240000100', 'cf:0001', '0001'
            put = "put 'test', '{}{}{}', 'cf:{}', '{}'"\
                .format(
                    DATE, (str(store)).zfill(5), (str(indicator)).zfill(2),
                    (str(minute)).zfill(4), (str(minute)).zfill(4)
                )
            SIO.write(put)
            SIO.write('\n')

    with open(data_file, 'wt') as file_o:
        file_o.write(SIO.getvalue())


if __name__ == '__main__':
    gen_one()
