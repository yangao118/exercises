#!/usr/bin/env python

import random

class Chipset(object):
    def __init__(self, index, val = 1):
        self.__state = val
        self.index = index

    @property
    def state(self):
        return self.__state

    def __str__(self):
        return str(self.state)

    def __repr__(self):
        return str((self.index, self.state))

    def test(self, other):
        if self.__state == 1:
            return other.__state
        else:
            return random.randint(0,1)

def jig(a, b):
    return (b.test(a), a.test(b))


def find_single_good(A):
    if len(A) <= 2:
        return A[0]

    mid = len(A) / 2

    pairs = zip(A[0:mid], A[mid:mid *2])

    kept = []

    for (a , b) in pairs:

        print a.index, b.index, a, b, jig(a,b)

        test_result = jig(a, b)

        if test_result == (1, 1):
            kept.append(a)
        elif test_result == (0, 0):
            pass
        elif test_result == (1, 0):
            kept.append(a)
        else:
            kept.append(b)


# Wrong! Think that by accident, each pair has one good and one bad

#    kept = [a for (a, b) in pairs if jig(a,b) == (1, 1)]

    if len(A) % 2 == 1:
        kept.append(A[-1])

    print kept

    return find_single_good(kept)



def main():


    chipsets = [Chipset(0, 1), Chipset(1, 1), Chipset(2, 0), Chipset(3, 0), Chipset(4, 1), Chipset(5, 0), Chipset(6, 1), Chipset(7, 1)]

    print chipsets

    single_good = find_single_good(chipsets)

    print single_good.index, single_good.state

    # This case the commented algorithm won't work
    chipsets2 = [Chipset(0, 0), Chipset(1, 1), Chipset(2, 0), Chipset(3, 0), Chipset(4, 1), Chipset(5, 0), Chipset(6, 1), Chipset(7, 1)]

    print chipsets2

    single_good = find_single_good(chipsets2)

    print single_good.index, single_good.state


if __name__ == "__main__":
    main()
