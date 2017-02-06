#!/usr/bin/env python

# Stack based on Fixed-length array

class stack(object):
    def __init__(self, n):
        self.top = -1
        self.size = n
        self.items = [ -1 for i in xrange(0, self.size) ]

    def push(self, x):
        if self.top >= self.size -1:
            print "stack overflow"
        else:
            self.top += 1
            self.items[self.top] = x

    def empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def pop(self):
        if self.pop == -1:
            print "stack underflow"
            return None
        else:
            self.top -= 1
            return self.items[self.top + 1]

    def __repr__(self):
        return "self.top= %d" % self.top \
            + str(self.items)

def main():
    s = stack(20)

    s.push(4)
    s.push(1)
    s.push(3)
    s.pop()
    s.push(8)
    s.pop()

    print s

if __name__ == "__main__":
    main()
