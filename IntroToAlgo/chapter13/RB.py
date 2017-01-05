#!/usr/bin/env python


class RBNode:
    red = 0
    black = 1

    def __init__(self, key):
        self.key = key
        self.p = None
        self.left = None
        self.right = None
        self.color = RBNode.red

    def __repr__(self):
        if self.color == RBNode.red:
            return "red: " + str(self.key)
        else:
            return "black: " + str(self.key)

class RBTree:
    def __init__(self):
        self.nil = RBNode(-1)
        self.nil.color = RBNode.black
        self.root = self.nil

def RB_inorder_walk(T, n):
    if n != T.nil:
        RB_inorder_walk(T, n.left)
        print n
        RB_inorder_walk(T, n.right)

def RB_preorder_walk(T, n):
    if n != T.nil:
        print n
        RB_preorder_walk(T, n.left)
        RB_preorder_walk(T, n.right)

def RB_postorder_walk(T, n):
    if n != T.nil:
        RB_postorder_walk(T, n.left)
        RB_postorder_walk(T, n.right)
        print n.key


def RB_seach(T, n, key):
    if n == T.nil or n.key == key:
        return n
    if n.key > key:
        return RB_seach(T, n.left, key)
    else:
        return RB_seach(T, n.right, key)

def RB_seach_iterative(T, n, key):
    while n != T.nil and n.key != key:
        if n.key > key:
            n = n.left
        else:
            n = n.right
    return n

def RB_min(T, n):
    while n != T.nil and n.left != T.nil:
        n = n.left
    return n

def RB_max(T, n):
    while n != T.nil and n.right != T.nil:
        n = n.right
    return n

def RB_successor(T, n):
    if n.right != T.nil:
        return RB_min(T, n.right)
    else:
        y = n.p
        while y != T.nil and n == y.right:
            n = y
            y = n.p
        return y

def RB_predecessor(T, n):
    if n.left != T.nil:
        return RB_max(T, n.left)
    else:
        y = n.p
        while y != T.nil and n == y.left:
            n = y
            y = n.p
        return y

def RB_transplant(T, u, v):
    if u.p == T.nil:
        T.root = v
    elif u == u.p.left:
        u.p.left = v
    else:
        u.p.right = v

    # Allows v is T.nil, also set parent
    # if v != T.nil:
    v.p = u.p

def RB_left_rotate(T, x):

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

def RB_right_rotate(T, x):

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

def RB_insert_fixup(T, z):
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
                    RB_left_rotate(T, z)

                # Now Case 3, zig-zig, rotate and recolor
                # And we're done!

                z.p.p.color = RBNode.red
                z.p.color = RBNode.black
                RB_right_rotate(T, z.p.p)

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
                    RB_right_rotate(T, z)

                # Now Case 3, zig-zig, rotate and recolor
                # And we're done!

                z.p.color = RBNode.black
                z.p.p.color = RBNode.red
                RB_left_rotate(T, z.p.p)

    T.root.color = RBNode.black



def RB_insert(T, n):

    x = T.root
    y = T.nil

    while x != T.nil:
        y = x
        if x.key > n.key:
            x = x.left
        else:
            x = x.right
    n.p = y
    if y == T.nil:
        T.root = n
    elif n.key > y.key:
        y.right = n
    else:
        y.left = n

    n.left = T.nil
    n.right = T.nil
    n.color = RBNode.red

    RB_insert_fixup(T, n)

def RB_delete_fixup(T, x):
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
                RB_left_rotate(T, x.p)
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
                    RB_right_rotate(T, w)
                    w = w.p

                # Casee 4:
                w.color = x.p.color
                x.p.color = RBNode.black
                w.right.color = RBNode.red

                RB_left_rotate(T, x.p)

                x = T.root

        # Class right

        else:

            w = x.p.left

            # Case 1
            if w.color == RBNode.red:
                x.p.color = RBNode.red
                w.color = RBNode.black
                RB_right_rotate(T, x.p)
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
                    RB_left_rotate(T, w)
                    w = x.p.left

                # Case 4:
                w.color = x.p.color
                x.p.color = RBNode.black
                w.left.color = RBNode.black

                RB_right_rotate(T, x.p)

                x = T.root

    # Now x node is red and carries an extra blackness, color it black

    x.color = RBNode.black

def RB_delete(T, z):

    # Keep track of these two nodes:
    # y is the node either removed from or moved within the tree
    # x is the node moved in to y's original position

    y = z
    y_original_color = z.color

    if z.left == T.nil:
        x = y.right
        RB_transplant(T, z, z.right)
    elif z.right == T.nil:
        x = y.left
        RB_transplant(T, z, z.left)
    else:
        y = RB_min(T, z.right)
        y_original_color = y.color
        x = y.right

        if y.p == z:

            # This extra assignment is to deal with the cast that x == T.nil

            x.p = y
        else:
            RB_transplant(T, y, y.right)
            y.right = z.right
            z.right.p = y

        RB_transplant(T, z, y)
        y.left = z.left
        y.left.p = y
        y.color = z.color

    if y_original_color == RBNode.black:
        RB_delete_fixup(T, x)


def RB_tests():
    T = RBTree()

    keys = [41, 38, 31, 12, 19, 8]

    for key in keys:
        node = RBNode(key)

        RB_insert(T, node)

    print "root: ", T.root

    RB_inorder_walk(T, T.root)

    RB_delete(T, T.root)

    RB_inorder_walk(T, T.root)

    for key in keys[::-1]:
        node = RB_seach(T, T.root, key)

        if node != T.nil:
            print "RB_delete ", node
            RB_delete(T, node)
            RB_inorder_walk(T, T.root)




if __name__ == "__main__":

    RB_tests()

