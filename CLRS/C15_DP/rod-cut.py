#!/usr/bin/env python

# Price table

price = [0, 1, 5 ,8 , 9, 10, 17, 17, 20, 24, 30]

# Recursive top-down

# O(2**n)

def cut_rod(p, n):
    if n == 0:
        return 0

    q = -1000

    for i in xrange(1, n+1):
        s = price[i] + cut_rod(p, n - i)
        if s > q:
            q = s

    return q


result = cut_rod(price, 10)

print result

# Memoization top-down method

def memoized_cut_rod_aux(p, n, r, s):
    if r[n] >= 0:
        return r[n]

    if n == 0:
        q = 0
    else:
        q = -1000

        for i in xrange(1, n+1):
            t = price[i] + memoized_cut_rod_aux(p, n - i, r, s)
            if t > q:
                q = t
                s[n] = i

    r[n] = q

    return q


def memoized_cut_rod(p, n):
    r = [ -1000 for i in xrange(n+1) ]
    s = [ -1 for i in xrange(n+1) ]

    memoized_cut_rod_aux(p, n, r, s)

    return (r, s)


# Bottom-up method

def bottom_up_cut_rod(p, n):

    r = [ -1000 for i in xrange(n+1) ]
    s = [ -1 for i in xrange(n+1) ]

    r[0] = 0

    for i in xrange(1, n+1):
        q = -1000

        for j in xrange(1, i+1):
            if q < price[j] + r[i - j]:
                q = price[j] + r[i - j]
                s[i] = j

        r[i] = q

    return (r, s)

def print_cut_rod_solution(n, r, s):

    while n > 0:
        print s[n]
        n = n - s[n]

(r, s) = memoized_cut_rod(price, 10)

print_cut_rod_solution(7, r, s)

(r, s) = bottom_up_cut_rod(price, 10)

print_cut_rod_solution(7, r, s)
