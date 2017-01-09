#!/usr/bin/env python

import sys

sys.path.append("../chapter13")

from RB import *

class OSTNode(RBNode):
    def __init__(self, key):
        RBNode.__init__(self, key)
        self.size = 0

    def __repr__(self):
        if self.color == RBNode.red:
            return "red: " + str(self.key) + " size: %d" % self.size
        else:
            return "black: " + str(self.key) + " size: %d" % self.size

class OST:
    def __init__(self):
        self.nil = OSTNode(-1)
        self.nil.size = 0
        self.nil.color = RBNode.black
        self.root = self.nil

def OST_left_rotate(T, x):

    y = x.right

    if y != T.nil:
        x.right = y.left
        if x.right != T.nil:
            x.right.p = x
        y.p = x.p
        if x.p == T.nil:
            T.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y

        x.p = y
        y.left = x
        y.size = x.size
        x.size = x.left.size + x.right.size + 1


def OST_right_rotate(T, x):


    y = x.left

    if y != T.nil:
        x.left = y.right
        if x.left != T.nil:
            x.left.p = x
        y.p = x.p
        if x.p == T.nil:
            T.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y

        x.p = y
        y.right = x
        y.size = x.size
        x.size = x.left.size + x.right.size + 1

def OST_insert_fixup(T, z):
    while z.p.color == RBNode.red:

        # Class A

        if z.p == z.p.p.left:
            y = z.p.p.right

            if y.color == RBNode.red:

                # Case 1, recolor

                z.p.color = RBNode.black
                y.color = RBNode.black
                z.p.p.color = RBNode.red

                z = z.p.p
            else:
                if z == z.p.right:

                    # Case 2, zig-zag, rotate

                    z = z.p
                    OST_left_rotate(T, z)

                # Now Case 3, zig-zig, rotate and recolor
                # And we're done!

                z.p.p.color = RBNode.red
                z.p.color = RBNode.black
                OST_right_rotate(T, z.p.p)

        # Class B

        else:
            y = z.p.p.left

            if y.color == RBNode.red:

                # Case 1, recolor

                z.p.color = RBNode.black
                y.color = RBNode.black
                z.p.p.color = RBNode.red

                z = z.p.p
            else:
                if z == z.p.left:

                    # Case 2, zig-zag, rotate

                    z = z.p
                    OST_right_rotate(T, z)

                # Now Case 3, zig-zig, rotate and recolor
                # And we're done!

                z.p.color = RBNode.black
                z.p.p.color = RBNode.red
                OST_left_rotate(T, z.p.p)

    T.root.color = RBNode.black



def OST_insert(T, n):

    x = T.root
    y = T.nil

    while x != T.nil:
        y = x

        # Should be here, otherwise root node is not updated
        x.size += 1
        if x.key > n.key:
            x = x.left
        else:
            x = x.right
        # x.size += 1

    n.p = y
    if y == T.nil:
        T.root = n
    elif y.key > n.key:

        # The test condition should be the same as the branching above
        # Otherwise will cause y.child be missing when y.key == n.key

        y.left = n
    else:
        y.right = n

    n.left = T.nil
    n.right = T.nil
    n.size = 1
    n.color = RBNode.red

    OST_insert_fixup(T, n)

def OST_delete_fixup(T, x):
    while x != T.root and x.color == RBNode.black:

        # Class left

        if x.p.left == x:

            # w must not be T.nil, because the black-height constaints
            # x carries an extra blackness

            w = x.p.right

            if w.color == RBNode.red:

                # Case 1: x.p must be black, rotate to make new w be black
                # New w is child of w, w is red, so new w is black

                x.p.color = RBNode.red
                w.color = RBNode.black
                OST_left_rotate(T, x.p)
                w = x.p.right

            if w.left.color == RBNode.black and w.right.color == RBNode.black:

                # Case 2: we remove w's blackness and x's extra blackness to its parent
                # And move to the parent, which carries the extra blackness now

                w.color = RBNode.red
                x = x.p
            else:

                if w.right.color == RBNode.black:

                # Case 3: rotate and recolor to enter case 4
                    w.left.color = RBNode.black
                    w.color = RBNode.red
                    OST_right_rotate(T, w)
                    w = w.p

                # Casee 4:
                w.color = x.p.color
                x.p.color = RBNode.black
                w.right.color = RBNode.red

                OST_left_rotate(T, x.p)

                x = T.root

        # Class right

        else:

            w = x.p.left

            # Case 1
            if w.color == RBNode.red:
                x.p.color = RBNode.red
                w.color = RBNode.black
                OST_right_rotate(T, x.p)
                w = x.p.left

            if w.left.color == RBNode.black and w.right.color == RBNode.black:

                # Case 2
                w.color = RBNode.red
                x = x.p
            else:

                if w.left.color == RBNode.black:

                    # Case 3
                    w.color = RBNode.red
                    w.right.color = RBNode.black
                    OST_left_rotate(T, w)
                    w = x.p.left

                # Case 4:
                w.color = x.p.color
                x.p.color = RBNode.black
                w.left.color = RBNode.black

                OST_right_rotate(T, x.p)

                x = T.root

    # Now x node is red and carries an extra blackness, color it black

    x.color = RBNode.black

def OST_transplant(T, u, v):
    if u.p == T.nil:
        T.root = v
    elif u == u.p.left:
        u.p.left = v
    else:
        u.p.right = v

    # Allows v is T.nil, also set parent
    # if v != T.nil:
    v.p = u.p

    if v != T.nil:
        v.size = u.size

def OST_delete(T, z):

    # Keep track of these two nodes:
    # y is the node either removed from or moved within the tree
    # x is the node moved in to y's original position

    y = z
    y_original_color = z.color

    if z.left == T.nil:
        x = y.right
        OST_transplant(T, z, z.right)
    elif z.right == T.nil:
        x = y.left
        OST_transplant(T, z, z.left)
    else:
        y = RB_min(T, z.right)
        y_original_color = y.color
        x = y.right

        if y.p == z:

            # This extra assignment is to deal with the cast that x == T.nil

            x.p = y
        else:
            OST_transplant(T, y, y.right)
            y.right = z.right
            z.right.p = y

        OST_transplant(T, z, y)
        y.left = z.left
        y.left.p = y
        y.color = z.color


    # Maintain size

    p = y

    while p != T.nil:
        p.size -= 1
        p = p.p


    if y_original_color == RBNode.black:
        OST_delete_fixup(T, x)


def OS_select(n, i):
    r = n.left.size + 1

    if r == i:
        return n
    elif r > i:
        return OS_select(n.left, i)
    else:
        return OS_select(n.right, i - r)

def OS_rank(T, x):
    r = x.left.size + 1

    y = x
    while y != T.root:
        if y == y.p.right:
            r += y.p.left.size + 1

        y = y.p

    return r

def OS_key_rank(T, n, k):
    try:
        if n.key == k:
            return n.left.size + 1
        elif n.key > k:
            return OS_key_rank(T, n.left, k)
        else:
            return OS_key_rank(T, n.right, k) + n.left.size + 1

    # Todo: How to deal with key is not in T?

    # Recursive exceptions in python

    except AttributeError as e:
        return 0


def OST_tests():

    keys = [ 26, 17, 41, 14, 21, 30, 47, 10, 16, 19, 21, 28, 38, 7, 12, 14, 20, 35, 39, 3 ]

    T = OST()

    for key in keys:
        node = OSTNode(key)
        OST_insert(T, node)

    RB_inorder_walk(T, T.root)

    print "OS_select: 10 ", OS_select(T.root, 10)
    print "OS_select: 12 ", OS_select(T.root, 12)

    print "OS_rank: 35 ", OS_rank(T, RB_search(T, T.root, 35))
    print "OS_key_rank: 38", OS_key_rank(T, T.root, 38)

    n2 = RB_search(T, T.root, 21)
    OST_delete(T, n2)

    print "\nOST_delete 21: "
    print "After deletion:\n"
    RB_inorder_walk(T, T.root)

    print "OS_select: 10 ", OS_select(T.root, 10)
    print "OS_select: 12 ", OS_select(T.root, 12)

    print "OS_rank: 35 ", OS_rank(T, RB_search(T, T.root, 35))
    print "OS_key_rank: 38", OS_key_rank(T, T.root, 38)

    print "OS_key_rank: 40", OS_key_rank(T, T.root, 40)


if __name__ == "__main__":

    OST_tests()
