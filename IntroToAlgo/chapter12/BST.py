#!/usr/bin/env python

import random

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.p = None
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.key)

class BST:
    def __init__(self):
        self.root = None

def BST_insert(T, n):

    y = None
    x = T.root

    while x != None:
        y = x

        # We can reload less equal for BSTNode,
        # for cases key is not comparable directly.

        if x.key > n.key:
            x = x.left
        else:
            x = x.right

    n.p = y

    if y == None:
        T.root = n
    elif y.key > n.key:
        y.left = n
    else:
        y.right = n

def BST_inorder_walk(n):
    if n != None:
        BST_inorder_walk(n.left)
        print n.key
        BST_inorder_walk(n.right)

class BlackBoxStack:
    def __init__(self):
        self.c = []

    def is_empty(self):
        return len(self.c) == 0

    def push(self, item):
        self.c.append(item)

    def pop(self):
        x = self.c[-1]

        del self.c[-1]
        return x

# Use auxiliary stack
# Please find more complicated version without stack in chapter10 exercises

def BST_inorder_walk_iterative(T):

    stack = BlackBoxStack()

    n = T.root

    while n != None:
        if n.left != None:
            stack.push(n)
            n = n.left
        else:
            print n.key
            if n.right != None:
                n = n.right
            else:
                while True:
                    if stack.is_empty():
                        n = None
                        break;

                    n = stack.pop()
                    print n.key

                    if n.right != None:
                        n = n.right
                        break

def BST_preorder_walk(n):
    if n != None:
        print n.key
        BST_preorder_walk(n.left)
        BST_preorder_walk(n.right)

def BST_postorder_walk(n):
    if n != None:
        BST_postorder_walk(n.left)
        BST_postorder_walk(n.right)
        print n.key

def randomly_build_BST(c):

    # Random permutaion

    for i in xrange(0, len(c)):
        j = random.randint(i, len(c) - 1)
        c[i], c[j] = c[j], c[i]

    T = BST()

    for item in c:
        node = BSTNode(item)
        BST_insert(T, node)

    return T

def BST_seach(n, key):
    if n == None or n.key == key:
        return n
    if n.key > key:
        return BST_seach(n.left, key)
    else:
        return BST_seach(n.right, key)

def BST_seach_iterative(n, key):
    while n != None and n.key != key:
        if n.key > key:
            n = n.left
        else:
            n = n.right
    return n

def BST_min(n):
    while n != None and n.left != None:
        n = n.left
    return n

def BST_max(n):
    while n != None and n.right != None:
        n = n.right
    return n

def BST_successor(n):
    if n.right != None:
        return BST_min(n.right)
    else:
        y = n.p
        while y != None and n == y.right:
            n = y
            y = n.p
        return y

def BST_predecessor(n):
    if n.left != None:
        return BST_max(n.left)
    else:
        y = n.p
        while y != None and n == y.left:
            n = y
            y = n.p
        return y

def BST_transplant(T, u, v):
    if u.p == None:
        T.root = v
    elif u == u.p.left:
        u.p.left = v
    else:
        u.p.right = v

    # Allows v is NULL
    if v != None:
        v.p = u.p

def BST_delete(T, n):
    # 4 cases:
    # No child
    # Only left child
    # Only right child
    # Left and right child
    if n.left == None:
        BST_transplant(T, n, n.right)
    elif n.right == None:
        BST_transplant(T, n, n.left)
    else:
        # We use predecessor here, textbook uses successor

        pre = BST_max(n.left)

        if pre != n.left:
            BST_transplant(T, pre, pre.left)
            pre.left = n.left
            n.left.p = pre

        BST_transplant(T, n, pre)
        pre.right = n.right
        n.right.p = pre


def BST_tests():

    c = [ i for i in xrange(20) ]

    T = randomly_build_BST(c)

    print "root node:"

    print T.root

    print "BST_inorder_walk:"
    BST_inorder_walk(T.root)

    print "BST_inorder_walk_iterative:"
    BST_inorder_walk_iterative(T)

    print "BST_preorder_walk:"
    BST_preorder_walk(T.root)

    print "BST_postorder_walk:"
    BST_postorder_walk(T.root)

    print "BST_seach: 10"
    n = BST_seach(T.root, 10)
    print n
    print BST_seach_iterative(T.root, 10)

    print "BST_successor: 10"
    print BST_successor(n)

    print "BST_predecessor: 10"
    print BST_predecessor(n)

    print "BST_delete: 10"
    BST_delete(T, n)

    print "BST_inorder_walk after deletion:"
    BST_inorder_walk(T.root)


    print "BST_max:"
    print BST_max(T.root)

    print "BST_min:"
    print BST_min(T.root)

if __name__ == "__main__":

    BST_tests()

