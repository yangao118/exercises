#!/usr/bin/env python

s = [-1, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]

f = [0, 4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]

def recursive_activity_selector(s, f, k, n):

    m = k + 1

    while m <= n and s[m] < f[k]:
        m = m + 1   # Find the first activity in Sk to finish,
                    # Sk means activities compatible after k finishes.

    if m <= n:
        return [m] + recursive_activity_selector(s, f, m, n)
    else:
        return []

def greedy_activity_selector(s, f):
    A = [1]
    k = 1

    for i in xrange(2, len(s)):
        if s[i] >= f[k]:
            A.append(i)
            k = i
    return A

def activity_selector_tests():

    result = recursive_activity_selector(s, f, 0, 11)
    print result

    result = greedy_activity_selector(s,f)
    print result

if __name__ == "__main__":
    activity_selector_tests()
