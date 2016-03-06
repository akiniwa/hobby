#! coding: utf-8
"""quick example"""
import pygraphviz as pgv


def agraph():
    """agraph"""
    g = pgv.AGraph()
    g.add_node('a')
    g.add_edge('b', 'c')
    print g

def load_dot_file():
    """load_dot_file"""
    g = pgv.AGraph("file.dot")
    print g

agraph()
