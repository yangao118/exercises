#!/usr/bin/env

import sys
sys.path.append('.')

from Graph import *

time = 0
topo = []

def DFS_visit(G, u):
    global time
    global topo

    time += 1
    u.d = time
    u.color = Vertex.gray

    for v in u.adj:
        if v.color == Vertex.white:
            v.p = u
            DFS_visit(G, v)
    time +=1
    u.f = time
    u.color = Vertex.black
    topo.append(u)


def DFS(G):
    global time

    for v in G.vertices:
        v.color = Vertex.white
        v.p = None
    time = 0

    for v in G.vertices:
        if v.color == Vertex.white:
            DFS_visit(G, v)

def DFS_tests():

    keys = "mnopqrstuvwxyz"
    vs = dict()
    G = Graph()

    for key in keys:
        vs[key] = Vertex(key)
        G.add_vertex(vs[key])

    vs['m'].add_adj(vs['q'])
    vs['m'].add_adj(vs['r'])
    vs['m'].add_adj(vs['x'])

    vs['n'].add_adj(vs['o'])
    vs['n'].add_adj(vs['q'])
    vs['n'].add_adj(vs['u'])

    vs['o'].add_adj(vs['r'])
    vs['o'].add_adj(vs['s'])
    vs['o'].add_adj(vs['v'])

    vs['p'].add_adj(vs['o'])
    vs['p'].add_adj(vs['s'])
    vs['p'].add_adj(vs['z'])

    vs['q'].add_adj(vs['t'])

    vs['r'].add_adj(vs['u'])
    vs['r'].add_adj(vs['y'])

    vs['s'].add_adj(vs['r'])

    vs['u'].add_adj(vs['t'])

    vs['v'].add_adj(vs['w'])
    vs['v'].add_adj(vs['x'])

    vs['w'].add_adj(vs['z'])

    vs['y'].add_adj(vs['v'])

    DFS(G)

    print topo

if __name__ == "__main__":

    DFS_tests()




