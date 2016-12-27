#!/usr/bin/env python

class BlackBoxStack:
    def __init__(self):
        self.s = []

    def is_empty(self):
        return len(self.s) == 0

    def push(self, x):
        self.s.append(x)

    def pop(self):
        x = self.s[-1]

        del self.s[-1]
        return x

class CompoundQueue:
    def __init__(self):
        self.stack_in = BlackBoxStack()
        self.stack_out = BlackBoxStack()

    def is_empty(self):
        return self.stack_in.is_empty() and self.stack_out.is_empty()

    def enqueue(self, x):
        self.stack_in.push(x)

    def dequeue(self):

		# Reuse the reverse stack till it's empty
        if self.stack_out.is_empty():
            if self.stack_in.is_empty():
                raise Exception('underflow')
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())
        return self.stack_out.pop()



class BlackBoxQueue:
	def __init__(self):
        self.q = []

    def is_empty(self):
        return len(self.q) == 0

    def enqueue(self, x):
        self.q.append(x)

    def dequeue(self):
        x = self.q[0]

        del self.q[0]
        return x

class CompoundStack:
    def __init__(self):
        self.queue_in = BlackBoxQueue()
        self.queue_out = BlackBoxQueue()

    def is_empty(self):
        return self.queue_in.is_empty()

    def push(self, x):
        self.queue_in.enqueue(x)

    # Exchange queue_in and queue_out, extract the last element
    def pop(self):
        if self.queue_in.is_empty():
            raise Exception("underflow")
        while True:
            x = self.queue_in.dequeue()
            if self.queue_in.is_empty():
                break
            self.queue_out.enqueue(x)

        self.queue_in, self.queue_out = self.queue_out, self.queue_in

        return x
