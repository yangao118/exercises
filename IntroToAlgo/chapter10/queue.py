#!/usr/bin/env python

# Queue based on fixed-length array

# Tail is pointed to the next postion for insertion will reduce the complexity.

class queue(object):
    def __init__(self, n):
        self.head = 0
        self.tail = 0
        self.size = n
        self.items = [ -1 for i in xrange(0, self.size) ]

    def enqueue(self, x):
        next_pos = (self.tail + 1) % self.size

        if next_pos == self.head:
            print "queue overflow"
        else:
            self.items[self.tail] = x
            self.tail = next_pos

    def dequeue(self):
        if self.head == self.tail:
            print "queue underflow"
            return None

        x = self.head
        self.head = (self.head + 1) % self.size

        return x

    def __repr__(self):
        return "self.head= %d, self.tail= %d\n" % (self.head, self.tail) \
            + str(self.items)

# This version is wrong
#
# It's the solution to Exercise 10.1-2, but not deque

class deque_bad(object):
    def __init__(self, n):
        self.front = -1
        self.back = n
        self.size = n
        self.items = [ -1 for i in xrange(0, self.size) ]

    def push_front(self, x):
        if self.front + 1 == self.back:
            print "deque overflow"
        else:
            self.front += 1
            self.items[self.front] = x

    def push_back(self, x):
        if self.back - 1 == self.front:
            print "deque overflow"
        else:
            self.back -= 1
            self.items[self.back] = x

    def pop_front(self):
        if self.front == -1:
            print "deque underflow"
            return None
        else:
            x = self.items[self.front]
            self.front -= 1
            return x

    def pop_back(self):
        if self.back == n:
            print "dequeue underflow"
            return None
        else:
            x = self.items[self.back]
            self.back += 1
            return x

class deque(object):
    def __init__(self, n):
        self.front = n / 2
        self.back = n / 2
        self.size = n
        self.items = [ -1 for i in xrange(0, self.size) ]
        print "self.front= %d, self.back= %d" % (self.front, self.back)

    def push_front(self, x):
        next_pos = (self.front + 1) % self.size
        if next_pos == self.back:
            print "deque overflow"
        else:
            self.items[self.front] = x
            self.front = next_pos
            print "push_front ", x, " self.front= %d" % self.front

    def push_back(self, x):
        next_pos = (self.back - 1 + self.size) % self.size
        if next_pos == self.front:
            print "deque overflow"
        else:
            self.items[self.back] = x
            self.back = next_pos
            print "push_back ", x, " self.back= %d" % self.back

    def pop_front(self):
        if self.front == self.back:
            print "deque underflow"
            return None
        else:
            x = self.items[self.front]
            self.front = (self.front - 1 + self.size) % self.size
            print "pop_front ", x, " self.front= %d" % self.front
            return x

    def pop_back(self):
        if self.back == self.front:
            print "dequeue underflow"
            return None
        else:
            x = self.items[self.back]
            self.back = (self.back + 1) % self.size
            print "pop_back ", x, " self.back= %d" % self.back
            return x


def test_queue():

    q = queue(6)

    q.enqueue(4)
    q.enqueue(1)
    q.enqueue(3)
    q.dequeue()
    q.enqueue(8)
    q.dequeue()

    print q

def test_deque():
    q = deque(10)

    q.push_front(1)
    q.push_front(2)
    q.push_front(3)
    q.push_front(4)
    q.push_front(5)
    q.push_front(6)
    q.push_front(7)
    q.push_front(8)
    q.push_front(9)
    q.push_front(10)
    q.push_front(11)
    q.push_front(12)

    q.pop_back()
    q.pop_back()
    q.pop_back()
    q.pop_back()
    q.pop_back()
    q.pop_back()
    q.pop_back()
    q.pop_back()
    q.pop_back()
    q.pop_back()
    q.pop_back()
    q.pop_back()

if __name__ == "__main__":
    test_queue()

    test_deque()



