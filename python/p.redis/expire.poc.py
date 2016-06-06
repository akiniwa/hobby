#! coding: utf-8

import redis

conn = redis.Redis(host='192.168.99.100', port=6379, db=1)
# False True True None
print conn.expire('not-exist-in-redis', 10)
print conn.set('exist-in-redis', 'now in redis')
print conn.expire('exist-in-redis', 0)
print conn.get('exist-in-redis')
