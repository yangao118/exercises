#!/usr/bin/env python

import random

def partition(A, p, r):
    key = A[p]
    i = p - 1

    for j in xrange(p + 1, r + 1):
        if A[j] < key:
            i += 1
            A[i] , A[j] = A[j], A[i]

    i += 1

    return i

def randomized_partition(A, p, r):
    i = random.randint(p, r)

    A[p], A[i] = A[i], A[p]

    return partition(A, p, r)

def randomized_select(A, p, r, i):
    if p == r:
        return A[p]

    q = randomized_partition(A, p, r)

    k = q - p + 1

    if i == k:
        return A[q]
    elif i < k:
        return randomized_select(A, p, q - 1, i)
    else:
        return randomized_select(A, q + 1, r, i - k)

def randomized_select_iterative(A, p, r, i):
    if p == r:
        return A[p]

    while True:

        q = randomized_partition(A, p, r)

        k = q - p + 1
        if i == k:
            return A[q]
        elif i < k:
            r = q -1
        else:
            p = q + 1
            i = i - k



def main():

    L = [ random.randint(0,10) for i in xrange(0, 20) ]

    print L

    print "randomized_select(L, 0, len(L) - 1, 5): ", randomized_select(L, 0, len(L) - 1, 5)

    print "randomized_select_iterative(L, 0, len(L) - 1, 5): ", randomized_select_iterative(L, 0, len(L) - 1, 5)

    print L

if __name__ == "__main__":
    main()
