#! coding: utf-8
'''python redis demo'''

import redis

RDS = redis.Redis('localhost')
# RDS = redis.Redis(host='localhost', port=6379, db=1)

def demo_info():
    '''demo info'''
    info = RDS.info()
    for key in info:
        print "%s: %s" % (key, info[key])

    # 查数据库大小
    print 'dbsize: %s' % RDS.dbsize()
    # 看连接
    print "ping %s" % RDS.ping()

    # 选数据库
    #r.select(2)
    # 移动数据去2数据库
    #r.move('a',2)
    # 其他
    #r.save('a') # 存数据
    #r.lastsave('a') # 取最后一次save时间
    #r.flush()  #刷新
    #r.shutdown() #关闭所有客户端，停掉所有服务，退出服务器

def demo_string():
    '''demo string'''
    # 塞数据
    RDS['c1'] = 'bar'
    #或者
    RDS.set('c2', 'bar')
    #这里有个 getset属性，如果为Tr 可以在存新数据时将上次存储内容同时搞出来
    print 'getset:', RDS.getset('c2', 'jj')
    #如果你想设置一个递增的整数 每执行一次它自加1：
    print 'incr:', RDS.incr('a')
    #如果你想设置一个递减的整数 please:
    print 'decr:', RDS.decr('a')
    # 取数据
    print 'r['']:', RDS['c1']
    #或者
    print 'get:', RDS.get('a')
    #或者 同时取一批
    print 'mget:', RDS.mget('c1', 'c2')
    #或者 同时取一批 它们的名字(key)很像 而恰好你又不想输全部
    print 'keys:', RDS.keys('c*')
    #又或者 你只想随机取一个：
    print 'randomkey:', RDS.randomkey()
    # 查看一个数据有没有 有 1 无0
    print 'existes:', RDS.exists('a')
    # 删数据 1是删除成功 0和None是没这个东西
    print 'delete:', RDS.delete('cc')
    # 哦对了 它是支持批量操作的
    print 'delete:', RDS.delete('c1', 'c2')
    #呃.改名
    RDS.rename('a', 'c3')
    #让数据10秒后过期 说实话我不太明白么意思
    RDS.expire('c3', 10)
    #看剩余过期时间 不存在返回-1
    RDS.ttl('c3')

def demo_list():
    '''demo list'''
    # 它是两头通的
    # 塞入
    RDS.lpush('b', 'gg')
    RDS.lpush('b', 'hh')
    # head 属性控制是不是从另一头塞
    RDS.rpush('b', 'ee')
    # 看长度
    print 'list len:', RDS.llen('b')
    # 列出一批出来
    print 'list lrange:', RDS.lrange('b', start=0, end=-1)
    # 取出一位
    print 'list index 0:', RDS.lindex('b', 0)
    # 修剪列表
    #若start 大于end,则将这个list清空
    print 'list ltrim :', RDS.ltrim('b', start=0, end=3) #只留 从0到3四位

def demo_set():
    '''demo set'''
    #--------------------------------
    # 集合(set)操作
    # 塞数据
    RDS.sadd('s', 'a')
    # 判断一个set长度为多少 不存在为0
    RDS.scard('s')
    # 判断set中一个对象是否存在
    RDS.sismember('s', 'a')
    # 求交集
    RDS.sadd('s2', 'a')
    RDS.sinter('s1', 's2')
    #求交集并将结果赋值
    RDS.sinterstore('s3', 's1', 's2')
    # 看一个set对象
    RDS.smembers('s3')
    # 求并集
    RDS.sunion('s1', 's2')
    # 阿 我想聪明的你已经猜到了
    #求并集 并将结果返回
    RDS.sunionstore('ss', 's1', 's2', 's3')
    # 求不同
    # 在s1中有，但在s2和s3中都没有的数
    RDS.sdiff('s1', 's2', 's3')
    RDS.sdiffstore('s4', 's1', 's2')# 这个你懂的
    # 取个随机数
    RDS.srandmember('s1')

def demo_zset():
    '''demo zset'''
    # RDS.zadd('demo_zset', 'a', 99.9)
    # RDS.zadd('demo_zset', 'b', 99.8)
    # RDS.zadd('demo_zset', 'c', 96.8)
    # RDS.zadd('demo_zset', 'd', 98.8)
    # RDS.zadd('demo_zset', 'e', 99.6)
    # RDS.zadd('demo_zset', 'f', 99.0)
    # RDS.zadd('demo_zset', 'g', 98.0)
    # RDS.zadd('demo_zset', 'h', 99.6)

    # print 'zrange:', RDS.zrange('demo_zset', 0, 4)
    for key in RDS.zrevrange('word_count', 0, -1):
        print RDS.zrevrank('word_count', key) + 1, key
    # print 'zrange:', RDS.zrangebyscore('demo_zset', 90, 100)

def demo_all():
    '''demo_all'''
    for i in xrange(1):
        RDS.set(i, i)
        print RDS.get(i)
        RDS.lpush('book', 'book1')
        RDS.lpush('book', 'book2')
        print 'list llen:', RDS.llen('book')
        print 'list lrange:', RDS.lrange('book', start=0, end=-1)
        print 'list index:', RDS.lindex('book', 1)
        RDS.sadd('litao', 'song1')
        RDS.sadd('litao', 'song2')
        print 'set scard:', RDS.scard('litao')
        print 'set sismember:', RDS.sismember('litao', 'song1')
        RDS.sadd('jingjie', 'song1')
        print 'sinter:', RDS.sinter('litao', 'jingjie')
        print 'set smembers:', RDS.smembers('litao')
        RDS.zadd(u'zset', 'litao', 2)
        RDS.zadd(u'zset', 'jingjie', 1)
        print 'zrange:', RDS.zrange('zset', 0, -1)
        print 'zrangebyscore:', RDS.zrangebyscore('zset', 1, 1)

# demo_info()
# demo_string()
# demo_list()
# demo_set()
demo_zset()
# demo_all()
