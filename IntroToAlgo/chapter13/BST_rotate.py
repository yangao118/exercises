#!/usr/bin/env python

import sys

sys.path.append("../chapter12")

from BST import *

def BST_left_rotate(T, x):

    y = x.right

    if y != None:
        x.right = y.left
        if x.right != None:
            x.right.p = x
        y.p = x.p
        if x.p == None:
            T.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y

        x.p = y
        y.left = x

def BST_right_rotate(T, x):

    y = x.left

    if y != None:
        x.left = y.right
        if x.left != None:
            x.left.p = x
        y.p = x.p
        if x.p == None:
            T.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y

        x.p = y
        y.right = x



def BST_rotate_tests():

    c = [ i for i in xrange(20) ]

    T = randomly_build_BST(c)

    print "root node:"

    print T.root

    print "BST_inorder_walk:"
    BST_inorder_walk(T.root)

    print "BST_seach: 10"
    n = BST_seach(T.root, 10)

    print "BST_left_rotate on ", n
    BST_left_rotate(T, n)

    print "BST_inorder_walk after left rotation:"
    BST_inorder_walk(T.root)

    n2 = BST_predecessor(n)
    print "BST_right_rotate on ", n2
    BST_right_rotate(T, n2)

    print "BST_inorder_walk after right rotation:"
    BST_inorder_walk(T.root)

if __name__ == "__main__":

    BST_rotate_tests()
