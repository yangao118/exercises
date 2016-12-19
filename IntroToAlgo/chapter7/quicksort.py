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

    return i

def randomized_partition(A, p, r):
    i = random.randint(p,r)
    A[i], A[r] = A[r], A[i]
    return partition(A, p, r)

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)

        # leave q alone, because it is in the right position
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)

def randomized_quicksort(A, p, r):
    if p < r:
        q = randomized_partition(A, p, r)

        # leave q alone, because it is in the right position
        randomized_quicksort(A, p, q - 1)
        randomized_quicksort(A, q + 1, r)

def tail_recursive_quicksort(A, p, r):
    while p < r:
        q = randomized_partition(A, p, r)
        tail_recursive_quicksort(A, p, q-1)
        p = q + 1

# To minimize the stack depth, we should loop for the larger partition
# and recusive call for the smaller partiontion

def tail_recursive_quicksort_min_stack_depth(A, p, r):
    while p < r:
        q = randomized_partition(A, p, r)
        if q < (q + r) / 2:
            tail_recursive_quicksort(A, p, q-1)
            p = q + 1
        else:
            tail_recursive_quicksort(A, q + 1, r)
            r = q - 1


def main():

    my_list = [ random.randint(0, 100) for i in xrange(0, 20) ]
    print my_list
    print "quicksort:"
    quicksort(my_list, 0, len(my_list) - 1)
    print my_list

    my_list = [ random.randint(0, 100) for i in xrange(0, 20) ]
    print my_list
    print "randomized_quicksort:"
    randomized_quicksort(my_list, 0, len(my_list) - 1)
    print my_list

    my_list = [ random.randint(0, 100) for i in xrange(0, 20) ]
    print my_list
    print "tail_recursive_quicksort:"
    tail_recursive_quicksort(my_list, 0, len(my_list) - 1)
    print my_list

    my_list = [ random.randint(0, 100) for i in xrange(0, 20) ]
    print my_list
    print "tail_recursive_quicksort_min_stack_depth:"
    tail_recursive_quicksort_min_stack_depth(my_list, 0, len(my_list) - 1)
    print my_list


if __name__ == "__main__":
    main()
