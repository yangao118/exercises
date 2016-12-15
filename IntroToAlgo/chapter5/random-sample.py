#!/usr/bin/env python

import random

def random_sample(m, n):
    if m == 0:
        return list()

    s = random_sample(m-1, n-1)
    i = random.randint(1,n)

    if i in s:
        s.append(n)
    else:
        s.append(i)

    return s

def main():
    print random_sample(5, 20)

if __name__ == "__main__":
    main()
