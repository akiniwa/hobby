# coding: utf-8

from time import sleep
from py2neo import Graph, Node, Relationship

graph = Graph(host='dc')
# graph = Graph(host='localhost', password='node')
# data = graph.data('MATCH (u:User) RETURN u limit 5')

# print data


def cleanup():
    """cleanup"""
    # delete rels
    print 'cleanup rels'
    graph.run("""
        MATCH ()-[h:HAS]->()
        DELETE h
    """)
    # delete nodes
    print 'cleanup nodes'
    graph.run("""
        MATCH (a:Area)
        DELETE a
    """)


def get_areas():
    """get_areas"""
    print('gen area data')
    with open('area.code.dat') as f:
        lines = f.readlines()

    areas = []

    areas.append(('-1', u'中华人民共和国', ''))

    for line in lines:
        (code, name) = line.strip().split(' ')
        if code.endswith('0' * 4):
            areas.append((code, name, '-1'))
        elif code.endswith('0' * 2):
            areas.append((code, name, code[:2] + '0' * 4))
        else:
            areas.append((code, name, code[:4] + '0' * 2))

    return areas


def create_nodes():
    """create_nodes"""
    print('create nodes')
    tx = graph.begin()

    for (code, name, pcode) in get_areas():
        node = Node('Area', code=code, name=name, pcode=pcode)
        tx.create(node)
        # sleep(1)
        # print 'add node', code, name, pcode

    tx.commit()


def create_relationships():
    """create_relationships"""
    print('create rels')
    graph.run("""
        MATCH (a:Area)
        MATCH (b:Area {code:a.pcode})
        CREATE (b)-[:HAS]->(a)
        """)

if __name__ == '__main__':
    cleanup()
    create_nodes()
    create_relationships()
