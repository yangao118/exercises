#!/usr/bin/env python

dim = [ 5, 10, 3, 12, 5, 50, 6 ]

def max_chain_order(dim):

    n = len(dim) - 1

    m = [ [ -1 for i in xrange(len(dim)) ] for i in xrange(len(dim)) ]

    solution = [ [ 0 for i in xrange(len(dim)) ] for i in xrange(len(dim)) ]

    for i in xrange(0, len(dim)):
        m[i][i] = 0

    for l in xrange(2, len(dim)):

        for i in xrange(1, len(dim) - l + 1):

            j = i + l - 1

            for k in xrange(i, j):
                q = m[i][k] + m[k + 1][j] + dim[i-1]*dim[k]*dim[j]

                if m[i][j] == -1 or q < m[i][j]:
                    m[i][j] = q
                    solution[i][j] = k

    return (m, solution)

def print_optimal_parens(s, i, j):

    if i == j:
        print "A%d" % i,
    else:
        print "(",
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print ")",

(m, s) = max_chain_order(dim)

for row in m:
    print row

for row in s:
    print row

print_optimal_parens(s, 1, 6)

