#!/usr/bin/env python

import copy
import random

def counting_sort(A,k):
    C = [0 for i in xrange(0, k + 1)]

    for j in xrange(0, len(A)):
        C[A[j]] += 1


    B = copy.deepcopy(A)

    if 1:
        # Naive way: looping in C

        # See problem 8-2.e
        # This way could sort in place, but not stable anymore

        x = 0;

        for n in xrange(0, k + 1):
            while C[n] > 0:
                B[x] = n
                x += 1
                C[n] -= 1
    else:
        # Smart way: prefix summing

        for k in xrange(1, k+1):
            C[k] += C[k-1]

        #print C


        for m in xrange(len(A) - 1, -1, -1):

            # Here subtract index by one because indexes start from 0

            B[C[A[m]] - 1] = A[m]
            C[A[m]] -= 1

    return B

def main():

    k = 10

    L = [ random.randint(0, 10) for i in xrange(0, 20) ]

    print L

    print "counting sort:"

    print counting_sort(L, 10)

if __name__ == "__main__":
    main()
