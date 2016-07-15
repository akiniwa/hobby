#! coding: utf-8
"""philosopher"""

import time
import logging
import threading
from contextlib import contextmanager

_local = threading.local()
logging.basicConfig(level=logging.INFO)


@contextmanager
def acquire(*locks):
    """acquire"""
    locks = sorted(locks, key=lambda x: id(x))
    acquired = getattr(_local, 'acquired', [])
    if acquired and max(id(lock) for lock in acquired) >= id(locks[0]):
        raise RuntimeError('lock order violation')

    acquired.extend(locks)
    _local.acquired = acquired
    try:
        for lock in locks:
            lock.acquire()
        yield
    finally:
        for lock in reversed(locks):
            lock.release()
        del acquired[-len(locks):]


def eating(left, right):
    """eating"""
    while True:
        with acquire(left, right):
            logging.info('%s %s', threading.currentThread(), 'eating')
            time.sleep(.5)

NSTICKS = 5

chopsticks = [threading.Lock() for n in range(NSTICKS)]

for n in range(NSTICKS):
    t = threading.Thread(target=eating,
                         args=(chopsticks[n], chopsticks[(n + 1) % NSTICKS]))
    t.start()
