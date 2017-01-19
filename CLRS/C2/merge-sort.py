#!/usr/bin/env python

# merge [p, q-1], [q, r] into [p, r]

def merge(array, p, q, r):

    left = array[p:q+1]
    right = array[q+1:r+1]

    i = 0
    j = 0

    for k in xrange(p, r + 1):
        if ((j == len(right)) or (i < len(left) and left[i] < right[j])):
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1

def merge_sort(array, p, r):
    if p < r:
        q = (p + r) / 2
        merge_sort(array, p, q)
        merge_sort(array, q + 1, r)
        merge(array, p, q, r)

def main():
    
    my_list = [3, 41, 52, 26, 38, 57, 9, 49]

    print "before sort: ", my_list
    merge_sort(my_list, 0, len(my_list) - 1)

    print "after sort: ", my_list

if __name__ == "__main__":
    main()
