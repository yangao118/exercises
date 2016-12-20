#!/usr/bin/env python

import random
import math

def insertion_sort(A):
    if len(A) <= 1:
        return

    for i in xrange(1, len(A)):
        key = A[i]

        for j in xrange(i - 1, -1, -1):
            if A[j] > key:
                A[j + 1] =  A[j]
            else:
                break

        A[j] = key

"""

Bucket sort has a auxiliary bucket array with n elements

The elements of A is ranged from 0 - Max, and are uniformly distributed.

We spilt them into n bucket, each bucket range from Max/n * i to Max/n * (i + 1)

The tricky part is that we may not know the Max...

So bucket sort's use case is restrictly limited.

"""

def bucket_sort(A, Max):

    B = [ list() for i in xrange(0, len(A) + 1) ]

    C = list()
    D = list()

    # Float not integer

    each_share = Max * 1.0 / len(A)

    for i in xrange(0, len(A)):
        B[int(math.floor(A[i] / each_share))].append(A[i])

    for j in xrange(0, len(A)):
        if len(B[j]) == 0:
            continue
        else:
            insertion_sort(B[j])
            C.append(B[j])
            D.extend(B[j])
    return C, D


def main():

    L = [random.randint(0, 10) for i in xrange(0, 20)]

    print L

    C, D = bucket_sort(L, 10)

    print C
    print D

if __name__ == "__main__":
    main()
