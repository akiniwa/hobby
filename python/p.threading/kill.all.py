#! coding: utf-8
"""kill.all.py"""

import logging
from Queue import Queue
from random import randint
from threading import Thread

logging.basicConfig(level=logging.INFO)

KILL = 0


def counter(name, count, queue):
    """counter"""
    logging.info(' thread %s work %s', name, count)
    while True:
        try:
            count -= 1
            # devide by zero
            _ = 5 // count
            logging.info(' thread %s calc %s', name, count)
            if not queue.empty() and KILL == queue.get(False):
                queue.put(KILL)
                break
            if 0 == count:
                queue.put(KILL)
                logging.info(' thread %s done %s', name, count)
                break
        except ArithmeticError:
            queue.put(KILL)
            logging.info(' thread %s exit %s', name, count)
            break


def main():
    """main"""
    my_q = Queue()

    threads = []
    for i in xrange(1, 10):
        thread = Thread(target=counter,
                        args=(i, randint(10, 30), my_q))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()
