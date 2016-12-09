#!/usr/bin/env python

def insertion_sort(array, start = 0, end = 0, inc = 1):
    if end == 0:
        end = len(array) - 1

    for i in xrange(start + 1, end + 1):
        # MIND HERE! xrange(s,e) ==> collection [s, e)
        j = i - 1
        key = array[i]

        if inc == 1:
            while j >= start and array[j] > key:
                array[j+1] = array[j]
                j -= 1
        else:
            while j >= start and array[j] < key:
                array[j+1] = array[j]
                j -= 1

        array[j+1] = key

def main():
    mylist = [31, 41, 59, 26, 41, 58]

    print "before sort:", mylist
    insertion_sort(mylist)
    print "after inc sort:", mylist
    insertion_sort(mylist, inc = 0)
    print "after dec sort:", mylist
    insertion_sort(mylist, 1, 4)
    print "after partial sort:", mylist

if __name__ == '__main__':
    main()
