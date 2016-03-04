#! coding: utf-8
"""networkx viz demo"""

import networkx as nx
import matplotlib.pyplot as plt


def plot(graphs):
    """plot"""
    nx.draw(graphs)
    plt.show()


def demo_draw():
    """demo_draw"""
    g = nx.Graph()
    g.add_edges_from([(1, 2), (1, 3)])
    g.add_node('sparm')
    plot(g)


def demo_save_fig():
    """demo_save_fig"""
    g = nx.Graph()
    g.add_edges_from([(1, 2), (1, 3)])
    g.add_node('sparm')
    nx.draw(g)
    nx.draw_random(g)
    nx.draw_circular(g)
    nx.draw_spectral(g)
    plt.savefig("g.png")


def demo_write_doc():
    """demo_write_doc"""
    g = nx.Graph()
    g.add_edges_from([(1, 2), (1, 3)])
    g.add_node('sparm')
    nx.draw(g)
    nx.draw_random(g)
    nx.draw_circular(g)
    nx.draw_spectral(g)
    nx.draw_graphviz(g)
    nx.write_dot(g, 'g.dot')


def demo_line():
    """demo_line"""
    g = nx.star_graph(10)
    l = nx.line_graph(g)
    plot(g)


def demo_karate():
    """demo_karate"""
    g = nx.karate_club_graph()
    plot(g)


def demo_complete():
    """demo_complete"""
    g = nx.complete_graph(20)
    plot(g)

# demo_draw()
# demo_save_fig()
# demo_write_doc()
# demo_line()
# demo_karate()
# demo_complete()
# plot(nx.grid_2d_graph(m=3, n=4))
# plot(nx.grid_graph(dim=[3, 4]))
# plot(nx.ladder_graph(5))
# plot(nx.lollipop_graph(m=3, n=4))
# plot(nx.wheel_graph(n=15))
# plot(nx.cycle_graph(n=15))
# plot(nx.balanced_tree(r=2, h=4))
# plot(nx.margulis_gabber_galil_graph(n=4))
# plot(nx.chordal_cycle_graph(p=4))
# plot(nx.bull_graph())
# plot(nx.diamond_graph())
# plot(nx.house_graph())
# plot(nx.pappus_graph())
# plot(nx.gnr_graph(n=5, p=5))
# plot(nx.gnc_graph(n=10))
# plot(nx.random_geometric_graph(n=10, radius=5))
# plot(nx.waxman_graph(n=10))
