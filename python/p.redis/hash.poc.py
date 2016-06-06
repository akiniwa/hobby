#! coding: utf-8

import redis

conn = redis.Redis(host='192.168.99.100', port=6379, db=1)
print conn.hset('key', 'f1', '1'), conn.hget('key', 'f1')
print conn.hsetnx('key', 'f1', '0'), conn.hget('key', 'f1')
print conn.expire('key', 0), conn.hget('key', 'f1')
