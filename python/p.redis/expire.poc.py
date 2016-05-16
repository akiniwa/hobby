#! coding: utf-8

import redis

conn = redis.Redis('localhost')
# False True True None
print conn.expire('not-exist-in-redis', 10)
print conn.set('exist-in-redis', 'now in redis')
print conn.expire('exist-in-redis', 0)
print conn.get('exist-in-redis')
