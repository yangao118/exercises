#!/usr/bin/evn python

import copy

class Vertex:
    white = 0
    gray = 1
    black = 2

    """
    Wrong! This will cause all vertices use the same adj declared in the parameter list!
    def __init__(self, key, adj = []):
        self.adj = adj
    """

    def __init__(self, key):
        self.adj = []
        self.key = key
        self.color = Vertex.white
        self.d = 0
        self.f = 0
        self.p = None

    def add_adj(self, v):
        self.adj.append(v)

    def __repr__(self):
        return "{key=%s, d=%d, f=%d, color=%d}" % (str(self.key), self.d, self.f, self.color)

class BlackBoxQueue:

    # deepcopy will eliminated the confusion in Vertex __init__
    def __init__(self, l = []):
        self.data = copy.deepcopy(l)

    def enqueue(self, v):
        self.data.append(v)

    def dequeue(self):
        tmp = self.data[0]
        del self.data[0]
        return tmp

    def empty(self):
        return len(self.data) == 0


class Graph:
    def __init__(self):
        self.vertices = []

    def add_vertex(self, v):
        self.vertices.append(v)

    def num_vertices(self):
        return len(self.vertices)
