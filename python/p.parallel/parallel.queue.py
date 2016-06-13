#! coding: utf-8
"""learning parallel"""

import sys
import time
import random
import re
import requests
import concurrent.futures
from multiprocessing import cpu_count, current_process, Manager, Process, Queue

import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(message)s')

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)


def producer_task(q, fibo_dict):
    """producer_task"""
    for i in range(15):
        value = random.randint(1, 20)
        fibo_dict[value] = None
        q.put(value)
        logger.info('producer [%s] put value [%d] into queue...'
                    % (current_process().name, value))
        q.put(value)


def consumer_task(q, fibo_dict):
    """consumer_task"""
    while not q.empty():
        value = q.get(True, 0.05)
        a, b = 0, 1
        for item in range(value):
            a, b = b, a + b
            fibo_dict[value] = a
        logger.info('consumer [%s] get value [%2d] from queue...'
                    % (current_process().name, value))


if __name__ == '__main__':
    data_queue = Queue()
    fibo_dict = {}
    producer = Process(target=producer_task, args=(data_queue, fibo_dict))
    producer.start()
    producer.join()

    consumer_list = []
    logger.info('cpu_count [%d]' % cpu_count())
    for i in range(cpu_count()):
        consumer = Process(target=consumer_task, args=(data_queue, fibo_dict))
        consumer.start()
        consumer_list.append(consumer)

    [consumer.join() for consumer in consumer_list]
    print fibo_dict
