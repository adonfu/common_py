# -*- coding:utf-8 -*-

"""
Test memory usage
"""

import objgraph



def cycle_ref():
    x = []
    y = [x, [x], dict(x=x)]

    objgraph.show_refs([y], filename='smaple-graph.png')
    objgraph.show_backrefs([x], filename='sample-backref-graph.png')
    objgraph.show_most_common_types()


if __name__ == '__main__':
    # cycle_ref()

    import pydot
    (graph,) = pydot.graph_from_dot_file('objgraph-dP_KLK.dot')
    graph.write_png('smaple-graph-dP_KLK.png')
