#!/usr/bin/env python

def swap(array, src, dest):
    tmp = array[src]
    array[src] = array[dest]
    array[dest] = tmp


# stable sorting

def selection_sort(array, start = 0, end = 0, inc = 1):

    if (end == 0):
        end = len(array) - 1

    for i in xrange(start, end):
        key = array[i]
        index = i
        for j in xrange(i, end + 1):
            if inc == 1:
                if array[j] < key:
                    key = array[j]
                    index = j
            else:
                if array[j] > key:
                    key = array[j]
                    index = j
        swap(array, i, index)


def main():
    array = [1, 4, 8 ,2, 3, 10, 2, 30]
    print "before sort: ", array
    selection_sort(array, 2, 5)
    print "partial sort: ", array
    selection_sort(array)
    print "after inc sort: ", array
    selection_sort(array, inc = 0)
    print "after dec sort: ", array

if __name__ == "__main__":
    main()
