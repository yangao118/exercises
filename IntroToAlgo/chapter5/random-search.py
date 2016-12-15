#!/usr/bin/env python

import random

def random_search(A, i):
    searched = set()
    counter = 0

    while (len(searched) < len(A)):
        counter += 1
        index = random.randint(0, len(A) - 1)

        if A[index] == i:
            return (index, counter)
        else:
            searched.add(index)

    return (-1, counter)

def main():

    my_list = [random.randint(0, 100) for i in xrange(0, 20)]

    print my_list

    print "random_search: key= 20 ", random_search(my_list, 20)

if __name__ == "__main__":
    main()
