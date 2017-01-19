#!/usr/bin/env python

# Disjoint forest is optimal for disjoint set, it's far better than linked-lists

class SetElement:
    def __init__(self, data):
        self.p = None
        self.rank = 0
        self.data = data
        self.next = None
        self.cardinality = 0

    def find_set(self):
        # Subtleties: two-pass method
        # As recursion winds, one pass up to the find path to find the root;
        # As recursion unwinds, one pass back to set the p to the root
        # Pass-compression heuristic: shorten the find path of the nodes in the path

        if self != self.p:
            self.p = self.p.find_set()

        # No else clause here
        return self.p

    def find_set_iterative(self):
        x = self
        while x != x.p:
            x = x.p

        root = x
        x = self
        while x != x.p:
            tmp = x.p
            x.p = root
            x = tmp

        return root

    def make_set(self):
        self.p = self
        self.rank = 0
        self.cardinality = 1
        self.next = self
        return self

    def union(self, y):

        # Union-by-rank heuristic: make the tree rather balanced
        def link(x, y):
            if x.rank > y.rank:
                y.p = x
                tmp = x.next
                x.next = y.next
                y.next = tmp
                x.cardinality += y.cardinality
                return x
            else:
                x.p = y
                tmp = x.next
                x.next = y.next
                y.next = tmp
                y.cardinality += x.cardinality

                if x.rank == y.rank:
                    y.rank += 1
                return y

        return link(self.find_set(), y.find_set())

    def __repr__(self):
        return "rank= %d, data= %s, cardinality= %d" % (self.rank, str(self.data), self.cardinality)

    def print_set(self):
        print self

        tmp = self.next

        while tmp != self:
            print tmp
            tmp = tmp.next


def disjoint_set_tests():

    elements = []

    for i in xrange(0, 16):

        elem = SetElement(i)
        elements.append(elem)
        elem.make_set()

    for i in xrange(0, 15, 2):
        elements[i].union(elements[i+1])

    for i in xrange(0, 13, 4):
        elements[i].union(elements[i+2])

    elements[0].union(elements[4])
    elements[10].union(elements[12])
    elements[0].union(elements[9])

    print "find_set_iterative x9: ", elements[9].find_set_iterative()
    print "find_set x1: ", elements[1].find_set()
    print "find_set x9: ", elements[9].find_set()

    print "\nprint_set start from set representative: "
    elements[0].find_set().print_set()
    print "\nprint_set start from element 5: "
    elements[5].print_set()

if __name__ == "__main__":
    disjoint_set_tests()


