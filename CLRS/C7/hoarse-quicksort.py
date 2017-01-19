#!/usr/bin/env python

import random

# Quick sort using hoarse partition is not stable sort either!
# Think about this array:
# 4 3 2 5 2 4 5 2 5


def hoare_partition(A, p, r):
    x = A[p]

    i = p - 1
    j = r + 1

    while True:
        j -= 1
        while A[j] > x:
            j -= 1
        i += 1
        while A[i] < x:
            i += 1
       #print i, j

        if i < j:
            A[i], A[j] = A[j], A[i]
        else:
            return j

def hoarse_quicksort(A, p, r):
    if p < r:
        q = hoare_partition(A, p, r)
        hoarse_quicksort(A, p, q)
        hoarse_quicksort(A, q + 1, r)


def main():
    l = [13, 19, 9, 5, 12, 8, 7, 4, 11, 2, 6, 21]

    print l

    print "hoare_partition:"

    print hoare_partition(l, 0, len(l) - 1)

    print l

    l = [ random.randint(0, 100) for i in xrange(0,20) ]

    print l

    print "hoarse_quicksort"

    hoarse_quicksort(l, 0, len(l) -1)

    print l


if __name__ == "__main__":
    main()
