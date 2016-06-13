#! coding: utf-8
"""learning parallel"""

import os
import random
from multiprocessing import Pipe, Process

import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(message)s')

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)


def producer_task(conn):
    """producer_task"""
    for i in range(5):
        value = random.randint(1, 10)
        conn.send(value)
        logger.info('producer pid [%s] send value [%d]...'
                    % (os.getpid(), value))
    conn.close()


def consumer_task(conn):
    """consumer_task"""
    for i in range(5):
        logger.info('consumer pid [%s] recv value [%d]...'
                    % (os.getpid(), conn.recv()))


if __name__ == '__main__':
    pconn, cconn = Pipe()
    consumer = Process(target=consumer_task, args=(cconn,))
    producer = Process(target=producer_task, args=(pconn,))

    consumer.start()
    producer.start()

    consumer.join()
    producer.join()
