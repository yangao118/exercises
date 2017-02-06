#!/usr/bin/env python

import random

# Quick sort using this is not stable sort!
# Think this array:
# 1 3 2 3 2 4 5 2
# The first 3 will end up after the second one.


def partition(A, p, r):
    key = A[r]

    i = p - 1

    for j in xrange(p, r):

        if A[j] <= key:
            i += 1
            A[i], A[j] = A[j], A[i]

    i += 1
    A[i], A[r] = A[r], A[i]

    j = i
    k = p - 1

    #print j, i
    #print A

    while True:
        while True:
            j -= 1
            if A[j] != key:
                break;

        while True:
            k += 1
            if A[k] == key:
                break;
        if k < j:
            A[j], A[k] = A[k], A[j]
        else:
            break
    return j + 1, i

# The method below is much better

def partition2(A, p, r):
    key = A[r]

    i = p - 1

    for j in xrange(p, r):

        if A[j] < key:
            i += 1
            A[i], A[j] = A[j], A[i]

    i += 1
    A[i], A[r] = A[r], A[i]

    j = i

    #print j, i
    #print A

    for k in xrange(i + 1, r - 1):
        if A[k] == key:
            j += 1
            A[k], A[j] = A[j], A[k]

    return i, j

def randomized_partition(A, p, r):
    i = random.randint(p,r)
    A[i], A[r] = A[r], A[i]
    return partition2(A, p, r)

def quicksort(A, p, r):
    if p < r:
        q1, q2  = randomized_partition(A, p, r)

        quicksort(A, p, q1 - 1)
        quicksort(A, q2 + 1, r)


def main():

    my_list = [ random.randint(0, 10) for i in xrange(0, 20) ]
    print my_list

    print "partition:"
    print partition2(my_list, 0, len(my_list) -1)
    print my_list

    print "quicksort"
    quicksort(my_list, 0, len(my_list) - 1)

    print my_list


if __name__ == "__main__":
    main()
