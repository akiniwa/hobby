import pygraphviz as pgv


def dot2png(file_dot):
    """dot2png"""
    G = pgv.AGraph(file_dot, rankdir="LR")
    G.layout(prog='dot')
    G.draw('{}.png'.format(file_dot))

# dot2png('read.demo.dot')
# dot2png('read.struct.dot')
# dot2png('read.cluster.dot')
dot2png('hbase.region.split.dot')
