#!/usr/bin/env python

import random

# Some notes: hight is from bottom to top

class MYHEAP(list):
    def __init__(self, i):
        self.__heap_size = 0
        list.__init__(self, i)

    @property
    def heap_size(self):
        return self.__heap_size
    @heap_size.setter
    def heap_size(self, value):
        self.__heap_size = value


# list index start from 0

def PARENT(i):
    return (i -1) / 2

def LEFT(i):
    return 2 * i + 1

def RIGHT(i):
    return 2 * i + 2

# Assume that left and right child are root of a max heap

def max_heapify(A, i):
    l = LEFT(i)
    r = RIGHT(i)

    if l < A.heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r < A.heap_size and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)

def min_heapify(A, i):
    l = LEFT(i)
    r = RIGHT(i)

    if l < A.heap_size and A[l] < A[i]:
        smallest = l
    else:
        smallest = i

    if r < A.heap_size and A[r] < A[smallest]:
        smallest = r

    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        min_heapify(A, smallest)

def build_max_heap(A):
    for i in xrange(PARENT(A.heap_size - 1), -1, -1):
        max_heapify(A, i)

def test_max_heapify():

    my_heap = MYHEAP([27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0])

    my_heap.heap_size = len(my_heap)

    print my_heap

    print "max_heapify(my_heap, 2):"

    max_heapify(my_heap, 2)

    print my_heap

def test_build_max_heap():

    my_heap = MYHEAP([5, 3, 17, 10, 84, 19, 6, 22, 9])

    my_heap.heap_size = len(my_heap)

    print my_heap

    print "build_max_heap(my_heap):"

    build_max_heap(my_heap)

    print my_heap

def heapsort(A):
    build_max_heap(A)

    for i in xrange(len(A) - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        A.heap_size -= 1
        max_heapify(A, 0)

def test_heapsort():
    my_heap = MYHEAP([5, 13, 2, 25, 7, 17, 20, 8, 4])

    my_heap.heap_size = len(my_heap)

    print my_heap

    print "heapsort(my_heap)"

    heapsort(my_heap)

    print my_heap

def heap_maximum(A):
    return A[0]

def heap_extract_max(A):
    if A.heap_size < 1:
        print "heap underflow"
        return None

    max = A[0]
    A[0] = A[A.heap_size - 1]
    A.heap_size -= 1
    del A[len(A) - 1]
    max_heapify(A, 0)

    return max

def heap_increase_key(A, i, key):
    if A[i] > key:
        print "new key is smaller than current key"
        return
    A[i] = key

    while i > 0 and A[PARENT(i)] < A[i]:
        A[PARENT(i)], A[i] = A[i], A[PARENT(i)]
        i = PARENT(i)

def max_heap_insert(A, key):
    A.append(-1000000)
    A.heap_size += 1
    heap_increase_key(A, A.heap_size - 1, key)

def heap_delete(A, i):
    A[i] = A[A.heap_size - 1]
    A.heap_size -= 1
    del A[A.heap_size]

    max_heapify(A, i)

def test_max_priority_queue():
    my_queue = MYHEAP([])

    for i in xrange(1, 20):
        max_heap_insert(my_queue, random.randint(0,100))

    print "after insert"
    print my_queue

    print "max"
    print heap_maximum(my_queue)

    print "after extract max"
    heap_extract_max(my_queue)
    print my_queue

    print "after extract max again"
    heap_extract_max(my_queue)
    print my_queue

    print "after heap delete 5"
    heap_delete(my_queue, 5)
    print my_queue



def main():
    test_max_heapify()

    test_build_max_heap()

    test_heapsort()

    test_max_priority_queue()

if __name__ == "__main__":
    main()
