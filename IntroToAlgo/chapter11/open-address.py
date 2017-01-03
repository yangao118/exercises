#!/usr/bin/env

m = 11

# Deletion: mark deleted item to a specific valule "Deleted"
# When insertion, Deleted equals to None, could be reused
# When searching, Deleted does not equal to None, searching continues

class LinearProbing:
    def __init__(self):
        global m
        self.t = [ None for i in xrange(0, m) ]

    def insert(self, key):
        global m

        for i in xrange(0, m):
            index = (key + i) % m

            if self.t[index] == None:
                self.t[index] = key
                break

    def search(self, key):
        global m

        ret = None
        for i in xrange(0, m):
            index = (key + i) % m

            if self.t[index] == None:
                break

            if self.t[index] == key:
                ret = index

        return ret

    def __repr__(self):
        return str(self.t)


class QuadraticProbing:
    def __init__(self):
        global m
        self.t = [ None for i in xrange(0, m) ]

    def insert(self, key):
        global m

        for i in xrange(0, m):
            index = (key + i + 3*i*i) % m

            if self.t[index] == None:
                self.t[index] = key
                break

    def search(self, key):
        global m

        ret = None
        for i in xrange(0, m):
            index = (key + i + 3*i*i) % m

            if self.t[index] == None:
                break

            if self.t[index] == key:
                ret = index

        return ret

    def __repr__(self):
        return str(self.t)

class DoubleHashing:
    def __init__(self):
        global m
        self.t = [ None for i in xrange(0, m) ]

    def insert(self, key):
        global m

        h2 = 1 + key % (m - 1)
        for i in xrange(0, m):
            index = (key + i * h2) % m

            if self.t[index] == None:
                self.t[index] = key
                break

    def search(self, key):
        global m

        ret = None
        h2 = 1 + key % (m - 1)
        for i in xrange(0, m):
            index = (key + i * h2) % m

            if self.t[index] == None:
                break

            if self.t[index] == key:
                ret = index

        return ret

    def __repr__(self):
        return str(self.t)


def test_open_address():
    keys = [ 10, 22, 31, 4, 15, 28, 17, 88, 59 ]
    linear = LinearProbing()

    for key in keys:
        linear.insert(key)

    print "LinearProbing: ", linear

    quadratic = QuadraticProbing()

    for key in keys:
        quadratic.insert(key)

    print "QuadraticProbing: ", quadratic

    double = DoubleHashing()

    for key in keys:
        double.insert(key)

    print "DoubleHashing: ", double

if __name__ == "__main__":
    test_open_address()
