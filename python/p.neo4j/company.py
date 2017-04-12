# coding: utf-8

from sets import Set
from py2neo import Graph, Node

graph = Graph(host='dco')
# graph = Graph(host='localhost')
# graph = Graph(host='localhost', password='node')
# data = graph.data('MATCH (u:User) RETURN u limit 5')

# print data


def cleanup():
    """cleanup"""
    # delete rels
    print 'cleanup rels'
    graph.run("""
        MATCH ()-[r:职务]->()
        DELETE r
    """)
    graph.run("""
        MATCH ()-[r:公司持股]->()
        DELETE r
    """)
    graph.run("""
        MATCH ()-[r:个人持股]->()
        DELETE r
    """)
    # delete nodes
    print 'cleanup nodes'
    graph.run("""
        MATCH (m:人员)
        DELETE m
    """)
    graph.run("""
        MATCH (m:公司)
        DELETE m
    """)
    # graph.run("""
    #     CREATE CONSTRAINT ON (m:Person) ASSERT m.code IS UNIQUE;
    # """)
    # graph.run("""
    #     CREATE CONSTRAINT ON (m:Company) ASSERT m.code IS UNIQUE;
    # """)
    # graph.run("""
    #     MATCH (m:PST)
    #     DELETE m
    # """)
    # graph.run("""
    #     MATCH (m:PSC)
    #     DELETE m
    # """)


def get_company():
    """get_company"""
    with open('data/company.csv') as f:
        lines = f.readlines()

    company = []

    for line in lines:
        company.append((line.strip().split(',')))
    return company


def create_company():
    """create_company"""
    print('create company')
    for (code, name) in get_company():
        graph.run("CREATE (a:公司 {代码: '%s', 名称: '%s'}) " % (code, name))


def get_position():
    """get_position"""
    with open('data/position.csv') as f:
        lines = f.readlines()

    position = []

    for line in lines:
        position.append((line.strip().split(',')))
    return position


def create_position():
    """create_position"""
    print('create position')
    person = Set([])
    for (code, name, _, _, _, _) in get_position():
        if code in person:
            continue
        person.add(code)
        graph.run("CREATE (a:职员 {代码: '%s', 名称: '%s'}) " % (code, name))

    for (code, name, pcode, pname, ccode, cname) in get_position():
        graph.run("""
            MATCH (a:职员 {代码: '%s'})
            MATCH (b:公司 {代码: '%s'})
            CREATE (b)-[:职务 {代码: '%s', 名称: '%s'} ]->(a)
            """ % (code, ccode, pcode, pname))


def get_stockholder():
    """get_stockholder"""
    with open('data/stockholder.csv') as f:
        lines = f.readlines()

    stockholder = []

    for line in lines:
        stockholder.append((line.strip().split(',')))
    return stockholder


def create_stockholder():
    """create_stockholder"""
    print('create stockholder')

    # 企业编码 企业名称 持股人编码 持股比例 持股人名称 持股标识
    for (ccode, _, code, percent, name, flag) in get_stockholder():
        if flag == "1":
            graph.run("""
                MATCH (a:职员 {代码: '%s'})
                MATCH (b:公司 {代码: '%s'})
                CREATE (b)-[:个人持股 {持股比例: '%s'} ]->(a)
                """ % (code, ccode, percent))
        else:
            graph.run("""
                MATCH (a:公司 {代码: '%s'})
                MATCH (b:公司 {代码: '%s'})
                CREATE (b)-[:公司持股 {持股比例: '%s'} ]->(a)
                """ % (code, ccode, percent))


if __name__ == '__main__':
    cleanup()
    create_company()
    create_position()
    create_stockholder()
