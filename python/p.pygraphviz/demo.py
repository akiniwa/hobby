#! coding: utf-8

import pygraphviz as pgv

nodes = [
    'assembly',
    'box',
    'box3d',
    'cds',
    'circle',
    'component',
    'cylinder',
    'diamond',
    'doublecircle',
    'doubleoctagon',
    'egg',
    'ellipse',
    'fivepoverhang',
    'folder',
    'hexagon',
    'house',
    'insulator',
    'invhouse',
    'invtrapezium',
    'invtriangle',
    'larrow',
    'lpromoter',
    'Mcircle',
    'Mdiamond',
    'Msquare',
    'none',
    'note',
    'noverhang',
    'octagon',
    'oval',
    'parallelogram',
    'pentagon',
    'plain',
    'plaintext',
    'point',
    'polygon',
    'primersite',
    'promoter',
    'proteasesite',
    'proteinstab',
    'rarrow',
    'rect',
    'rectangle',
    'restrictionsite',
    'ribosite',
    'rnastab',
    'rpromoter',
    'septagon',
    'signature',
    'square',
    'star',
    'tab',
    'terminator',
    'threepoverhang',
    'trapezium',
    'triangle',
    'tripleoctagon',
    'underline',
    'utr',
]


def node_shape():
    """node_shape"""
    G = pgv.AGraph()
    for node in nodes:
        G.add_node(node)
        n = G.get_node(node)
        n.attr['shape'] = node
    G.layout(prog='dot')
    G.draw('node.shape.png')

node_shape()
