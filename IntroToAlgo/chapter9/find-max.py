#!/usr/bin/env python

import random

def find_max_and_min(A):
    if len(A) % 2 == 1:
        max, min = A[0], A[0]
        i = 1
    else:
        if A[0] > A[1]:
            max, min = A[0], A[1]
        else:
            max, min = A[1], A[0]
        i = 2


    while (i < len(A) - 1):
        if A[i] > A[i+1]:
            if A[i] > max:
                max = A[i]
            if A[i+1] < min:
                min = A[i+1]
        else:
            if A[i+1] > max:
                max = A[i+1]
            if A[i] < min:
                min = A[i]
        i += 2

    return max, min

# Tournament style

class player(object):
    def __init__(self, value):
        self.value = value
        self.opponents = list()

    def match(self, other):
        self.opponents.append(other)
        other.opponents.append(self)
        if (self.value >= other.value):
            return self
        else:
            return other

def tournament(A):
    if len(A) == 1:
        return A[0]

    winners = list()
    i = 0;

    while i <= len(A) - 1:
        if (i + 1 <= len(A) - 1):
            winners.append(A[i].match(A[i+1]))
            i += 2
        else:
            winners.append(A[i])
            mingle = random.randint(0, len(winners) - 1)
            winners[mingle], winners[len(winners) - 1] = winners[len(winners) - 1], winners[mingle]

            i += 1

    return tournament(winners)


# Need a data structure to record each match
def find_second_largest(A):

    champion = tournament(A)

    print "champion %d" % champion.value

    second = champion.opponents[0]

    for i in xrange(0, len(champion.opponents) - 1):
        if champion.opponents[i].value > second.value:
            second = champion.opponents[i]

    print "second place: %d" % second.value

    return second


def main():

    L = [ random.randint(0,20) for i in xrange(0,30) ]

    print L

    print "find_max_and_min: ", find_max_and_min(L)

    players = [ player(L[i]) for i in xrange(0,30) ]

    find_second_largest(players)



if __name__ == "__main__":
    main()
