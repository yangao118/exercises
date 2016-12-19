#!/usr/bin/env python

import random

# Quicksort taken from equal-quicksort.py

def partition(A, p, r):
    key = A[r]

    i = p - 1

    for j in xrange(p, r):

        if A[j] < key:
            i += 1
            A[i], A[j] = A[j], A[i]

    i += 1
    A[i], A[r] = A[r], A[i]

    j = i

    for k in xrange(i + 1, r - 1):
        if A[k] == key:
            j += 1
            A[k], A[j] = A[j], A[k]

    return i, j

def randomized_partition(A, p, r):
    i = random.randint(p,r)
    A[i], A[r] = A[r], A[i]
    return partition(A, p, r)

def quicksort(A, p, r):
    if p < r:
        q1, q2  = randomized_partition(A, p, r)

        quicksort(A, p, q1 - 1)
        quicksort(A, q2 + 1, r)

class fuzzy(object):
    def __init__(self, low, interval):
        self.low = low
        self.high = low + interval

    def __eq__(self, other):
        return max(self.low, other.low) <= min(self.high, other.high)

    def __lt__(self, other):
        return self.low < other.low

    def __repr__(self):
        return "(%d, %d)" % (self.low, self.high)

def main():

    L = [ fuzzy(random.randint(0,20), random.randint(0,10)) for i in xrange(0,20) ]

    print L

    print "fuzzy_quicksort:"

    quicksort(L, 0, len(L) - 1)

    print L



if __name__ == "__main__":
    main()
