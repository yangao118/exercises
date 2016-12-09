#!/usr/bin/env python

def binary_search(A, p, r, v):
    print "p=%d, r=%d, v=%d" % (p, r, v)
    if p < r:
        q = (p + r) / 2

        if A[q] == v:
            return q
        elif A[q] > v:
            return binary_search(A, p, q - 1, v)
        else:
            return binary_search(A, q + 1, r, v)
    else:
        if A[p] == v:
            return p
        else:
            return -1

def main():

    sorted_array = [1, 2, 4, 7, 8, 21, 24, 30, 49, 51, 52, 54, 60]

    print sorted_array

    for x in (5, 1, 30 ,60):
        ret_val = binary_search(sorted_array, 0, len(sorted_array) -1, x)
        print "searching %d: %d" % (x, ret_val)

#    print "searching 5: " ,binary_search(sorted_array, 0, len(sorted_array) -1, 5)

#    print "searching 1: " ,binary_search(sorted_array, 0, len(sorted_array) -1, 1)

#    print "searching 30: " ,binary_search(sorted_array, 0, len(sorted_array) -1, 30)

#    print "searching 60: " ,binary_search(sorted_array, 0, len(sorted_array) -1, 60)

if __name__ == "__main__":
    main()
