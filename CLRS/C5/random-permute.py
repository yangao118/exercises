#!/usr/bin/env python

import random

def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp

def random_permute(A):
    for i in xrange(0, len(A)):
        swap(A, i, random.randint(i, len(A) - 1))


def main():
    listmy = [ i for i in xrange(1, 20) ]
    print listmy

    random_permute(listmy)

    print listmy

if __name__ == "__main__":
    main()

