#!/usr/bin/env python

import sys
sys.path.append('.')

from Graph import *

def BFS(G, s):

    for v in G.vertices:
        v.color = Vertex.white
        v.d = sys.maxint
        v.p = None

    s.color = Vertex.gray
    s.d = 0
    s.p = None

    q = BlackBoxQueue()

    q.enqueue(s)

    while not q.empty():
        u = q.dequeue()

        for v in u.adj:
            if v.color == Vertex.white:
                v.color = Vertex.gray
                v.d = u.d + 1
                v.p = u
                q.enqueue(v)
        u.color = Vertex.black

def print_path(G, s, v):
    if v == s:
        print s
    elif v.p is None:
        print "no path from ", s, "to", v, "exists"
    else:
        print_path(G, s, v.p)
        print v


def BFS_tests():

    keys = [ 'r', 's', 't', 'u', 'v', 'w', 'x', 'y' ]

    vs = dict()

    for key in keys:
        vs[key] = Vertex(key)

    vs['r'].add_adj(vs['s'])
    vs['r'].add_adj(vs['v'])

    vs['s'].add_adj(vs['r'])
    vs['s'].add_adj(vs['w'])

    vs['t'].add_adj(vs['w'])
    vs['t'].add_adj(vs['u'])
    vs['t'].add_adj(vs['x'])

    vs['u'].add_adj(vs['t'])
    vs['u'].add_adj(vs['x'])
    vs['u'].add_adj(vs['y'])

    vs['v'].add_adj(vs['r'])

    vs['w'].add_adj(vs['s'])
    vs['w'].add_adj(vs['t'])
    vs['w'].add_adj(vs['x'])

    vs['x'].add_adj(vs['w'])
    vs['x'].add_adj(vs['t'])
    vs['x'].add_adj(vs['y'])
    vs['x'].add_adj(vs['u'])

    vs['y'].add_adj(vs['u'])
    vs['y'].add_adj(vs['x'])

    G = Graph()

    for v in vs.values():
        G.add_vertex(v)

    BFS(G, vs['s'])
    print_path(G, vs['s'], vs['u'])

if __name__ == "__main__":

    BFS_tests()
