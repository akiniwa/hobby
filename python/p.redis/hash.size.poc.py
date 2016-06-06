#! coding: utf-8
"""hash size poc"""

import redis
import time

conn = redis.Redis(host='192.168.99.100', port=6379, db=1)

key = '1234567890_1234567_12345678_12345678'
base = 1000000000


def hash_size_poc():
    """hash_size_poc"""
    print conn.info()
    for skuid in range(310925):
        conn.hset(key, str(base + skuid), time.time())
    # {
    #     "encoding": "hashtable",
    #     "refcount": 1,
    #     "lru_seconds_idle": 0,
    #     "lru": 4453566,
    #     "at": "0x7f0fafe608b0",
    #     "serializedlength": 6184428,
    #     "type": "Value"
    # }
    print conn.debug_object(key)
    print conn.info()
    conn.expire(key, 0)

hash_size_poc()
