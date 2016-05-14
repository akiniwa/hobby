#! coding: utf-8
'''python redis demo'''

import redis

# conn = redis.Redis('localhost')
conn = redis.Redis(host='172.17.0.3', port=6379, db=1)

def demo_info():
    '''demo info'''
    info = conn.info()
    for key in info:
        print "%s: %s" % (key, info[key])

    # 查数据库大小
    print 'dbsize: %s' % conn.dbsize()
    # 看连接
    print "ping %s" % conn.ping()

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
    conn['c1'] = 'bar'
    #或者
    conn.set('c2', 'bar')
    #这里有个 getset属性，如果为Tr 可以在存新数据时将上次存储内容同时搞出来
    print 'getset:', conn.getset('c2', 'jj')
    #如果你想设置一个递增的整数 每执行一次它自加1：
    print 'incr:', conn.incr('a')
    #如果你想设置一个递减的整数 please:
    print 'decr:', conn.decr('a')
    # 取数据
    print 'r['']:', conn['c1']
    #或者
    print 'get:', conn.get('a')
    #或者 同时取一批
    print 'mget:', conn.mget('c1', 'c2')
    #或者 同时取一批 它们的名字(key)很像 而恰好你又不想输全部
    print 'keys:', conn.keys('c*')
    #又或者 你只想随机取一个：
    print 'randomkey:', conn.randomkey()
    # 查看一个数据有没有 有 1 无0
    print 'existes:', conn.exists('a')
    # 删数据 1是删除成功 0和None是没这个东西
    print 'delete:', conn.delete('cc')
    # 哦对了 它是支持批量操作的
    print 'delete:', conn.delete('c1', 'c2')
    #呃.改名
    conn.rename('a', 'c3')
    #让数据10秒后过期 说实话我不太明白么意思
    conn.expire('c3', 10)
    #看剩余过期时间 不存在返回-1
    conn.ttl('c3')

def demo_list():
    '''demo list'''
    # 它是两头通的
    # 塞入
    conn.lpush('b', 'gg')
    conn.lpush('b', 'hh')
    # head 属性控制是不是从另一头塞
    conn.rpush('b', 'ee')
    # 看长度
    print 'list len:', conn.llen('b')
    # 列出一批出来
    print 'list lrange:', conn.lrange('b', start=0, end=-1)
    # 取出一位
    print 'list index 0:', conn.lindex('b', 0)
    # 修剪列表
    #若start 大于end,则将这个list清空
    print 'list ltrim :', conn.ltrim('b', start=0, end=3) #只留 从0到3四位

def demo_set():
    '''demo set'''
    #--------------------------------
    # 集合(set)操作
    # 塞数据
    conn.sadd('s', 'a')
    # 判断一个set长度为多少 不存在为0
    conn.scard('s')
    # 判断set中一个对象是否存在
    conn.sismember('s', 'a')
    # 求交集
    conn.sadd('s2', 'a')
    conn.sinter('s1', 's2')
    #求交集并将结果赋值
    conn.sinterstore('s3', 's1', 's2')
    # 看一个set对象
    conn.smembers('s3')
    # 求并集
    conn.sunion('s1', 's2')
    # 阿 我想聪明的你已经猜到了
    #求并集 并将结果返回
    conn.sunionstore('ss', 's1', 's2', 's3')
    # 求不同
    # 在s1中有，但在s2和s3中都没有的数
    conn.sdiff('s1', 's2', 's3')
    conn.sdiffstore('s4', 's1', 's2')# 这个你懂的
    #
    conn.srandmember('s1')

def demo_zset():
    '''demo zset'''
    # conn.zadd('demo_zset', 'a', 99.9)
    # conn.zadd('demo_zset', 'b', 99.8)
    # conn.zadd('demo_zset', 'c', 96.8)
    # conn.zadd('demo_zset', 'd', 98.8)
    # conn.zadd('demo_zset', 'e', 99.6)
    # conn.zadd('demo_zset', 'f', 99.0)
    # conn.zadd('demo_zset', 'g', 98.0)
    # conn.zadd('demo_zset', 'h', 99.6)

    # print 'zrange:', conn.zrange('demo_zset', 0, 4)
    for key in conn.zrevrange('word_count', 0, -1):
        print conn.zrevrank('word_count', key) + 1, key
    # print 'zrange:', conn.zrangebyscore('demo_zset', 90, 100)

def demo_all():
    '''demo_all'''
    for i in xrange(1):
        conn.set(i, i)
        print conn.get(i)
        conn.lpush('book', 'book1')
        conn.lpush('book', 'book2')
        print 'list llen:', conn.llen('book')
        print 'list lrange:', conn.lrange('book', start=0, end=-1)
        print 'list index:', conn.lindex('book', 1)
        conn.sadd('litao', 'song1')
        conn.sadd('litao', 'song2')
        print 'set scard:', conn.scard('litao')
        print 'set sismember:', conn.sismember('litao', 'song1')
        conn.sadd('jingjie', 'song1')
        print 'sinter:', conn.sinter('litao', 'jingjie')
        print 'set smembers:', conn.smembers('litao')
        conn.zadd(u'zset', 'litao', 2)
        conn.zadd(u'zset', 'jingjie', 1)
        print 'zrange:', conn.zrange('zset', 0, -1)
        print 'zrangebyscore:', conn.zrangebyscore('zset', 1, 1)

demo_info()
# demo_string()
# demo_list()
# demo_set()
# demo_zset()
# demo_all()
