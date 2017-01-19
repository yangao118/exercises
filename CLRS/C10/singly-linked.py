#!/usr/bin/env python

class SinglyLinkedList:
    def __init__(self, key):
        self.key = key
        self.next = None

    def __repr__(self):
        return "key %d, next %d" % (self.key, id(self.next))

# We use a head hasing key -1 as sentinel for simplicity

def insert(head, x):
    x.next = head.next
    head.next = x

def list_search(head, key):
    iter = head.next
    while iter != None:
        if iter.key == key:
            break
        iter = iter.next
    return iter

def delete(head, x):
    iter = head

    while iter != None:
        if id(iter.next) == id(x):
            break;
        iter = iter.next

    iter.next = x.next
    del x

def show(head):
    iter = head.next
    i = 1

    while iter != None:
        print "%d element: %d" % (i, iter.key)
        i += 1
        iter = iter.next

def is_empty(head):
    return head.next == None

def reverse(head):
    prev = head
    now = prev.next

    while now != None:
        next = now.next
        if id(prev) == id(head):
            now.next = None
        else:
            now.next = prev

        prev = now
        now = next

    head.next = prev

def test_singly_linked_list():

    S = SinglyLinkedList(-1)

    for i in xrange(1, 6):
        x = SinglyLinkedList(i)
        insert(S, x)

    show(S)

    y = list_search(S, 1)

    print y

    delete(S, y)

    show(S)

    print "Reverse:"

    reverse(S)

    print S

    show(S)




class ListBasedStack:
    def __init__(self):
        self.head = SinglyLinkedList(-1)

    def is_empty(self):
        return is_empty(self.head)

    def push(self, key):
        x = SinglyLinkedList(key)
        insert(self.head, x)

    def pop(self):
        if is_empty(self.head):
            print "stack underflow"
            return None
        else:
            x = self.head.next
            self.head.next = x.next

            return x.key

def test_list_based_stack():
    S = ListBasedStack()

    S.push(0)
    S.push(3)
    S.push(4)

    print S.pop()
    print S.pop()
    print S.pop()

    print S.pop()

class ListBasedQueue:
    def __init__(self):
        self.head = SinglyLinkedList(-1)
        self.tail = self.head

    def is_empty(self):
        return is_empty(self.head)

    def enqueue(self, key):
        x = SinglyLinkedList(key)
        insert(self.tail, x)
        self.tail = x

    def dequeue(self):
        if is_empty(self.head):
            print "stack underflow"
            return None
        else:
            x = self.head.next
            self.head.next = x.next

            return x.key

def test_list_based_queue():
    Q = ListBasedQueue()

    Q.enqueue(0)
    Q.enqueue(3)
    Q.enqueue(4)

    print Q.dequeue()
    print Q.dequeue()
    print Q.dequeue()

    print Q.dequeue()


if __name__ == "__main__":
    test_singly_linked_list()

    test_list_based_stack()

    test_list_based_queue()
