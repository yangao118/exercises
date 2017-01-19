#!/usr/bin/env python

# -O means optimization mode, which will turn off __debug__

class BTreeNode:
    def __init__(self, t):
        self.leaf = False
        self.n = 0
        self.keys = [ None for i in xrange(t * 2 - 1) ]
        self.children = [ None for i in xrange(t * 2) ]

    # Normally, a BTreeNode is fixed size according to the I/O unit
    # for the underlying diskes. A whole B-Tree is very huge and cannot
    # fit in DRAM memory, we only keep root and some other nodes in mem,
    # and read/write other node from/to disk as needed.

    # B-Tree usually is a basic structure for some databases & file systems

    def disk_read(self):

        # Dummy function simulates read a page containing a BTreeNode
        # from disk

        pass

    def disk_write(self):

        # Dummy function simulates write a BTreeNode to a disk page

        pass

    def __repr__(self):

        return "leaf: " + str(self.leaf) + "\n" \
            + "number of keys: %d" % self.n + "\n" \
            + "keys: " + str(self.keys) + "\n"


class BTree:
    def __init__(self, t):
        self.t = t
        self.height = 0
        self.root = BTreeNode(t)
        self.root.leaf = True
        self.nodes = 1

    def search(self, key):

        # Return a stack of reached nodes to compute predecessor or successor

        def search_sub(x, key, stack):
            i = 0

            while i < x.n and x.keys[i] < key:
                i += 1

            if i < x.n and x.keys[i] == key:
                return (x, i)

            if x.leaf:
                return (None, 0)
            else:
                stack.append(x)
                x.children[i].disk_read()
                return search_sub(x.children[i], key, stack)

        stack = []

        return (search_sub(self.root, key, stack), stack)

    def split_child(self, x, i):

        z = BTreeNode(self.t)
        self.nodes += 1
        y = x.children[i]

        if __debug__:
            print "before split_child: "
            print "x: ", x
            print "y: ", y

        z.n = self.t - 1
        z.leaf = y.leaf

        # Copy the upper half of y into z

        for j in xrange(0, z.n):
            z.keys[j] = y.keys[self.t + j]
            y.keys[self.t + j] = None

        if not z.leaf:
            for j in xrange(0, z.n + 1):
                z.children[j] = y.children[self.t + j]
                y.children[self.t + j] = None

        y.n = self.t - 1

        for j in xrange(x.n - 1, i - 1, -1):
            x.keys[j + 1] = x.keys[j]

        # Dont use j here, for j maybe not initialized when x.n == i
        x.keys[i]  = y.keys[self.t - 1]
        y.keys[self.t - 1] = None

        for j in xrange(x.n, i, -1):
            x.children[j + 1] = x.children[j]

        # Dont use j here, for j maybe not initialized when x.n == i
        x.children[i + 1] = z

        x.n += 1

        x.disk_write()
        y.disk_write()
        z.disk_write()

        if __debug__:
            print "after split_child: "
            print "x: ", x

            print "x.children[i]: ", x.children[i]
            print "x.children[i+1]: ", x.children[i + 1]

    def insert_nofull(self, x, key):

        if __debug__:
            print "insert_nofull: ", key
            print x

        i = x.n - 1

        if x.leaf:
            while i >= 0 and x.keys[i] > key:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = key
            x.n += 1
            x.disk_write()

            if __debug__:
                print "leaf insert_nofull: ", key
                print x

        else:

            while i >= 0 and x.keys[i] > key:
                i -= 1

            i = i + 1

            n = x.children[i]
            n.disk_read()

            if n.n == 2 * self.t - 1:
                self.split_child(x, i)

                if key > x.keys[i]:
                    i += 1

            self.insert_nofull(x.children[i], key)


    def insert(self, key):
        r = self.root

        if r.n == 2 * self.t  - 1:
            n = BTreeNode(self.t)
            n.leaf = False
            n.children[0] = r

            self.root = n
            self.height += 1
            self.nodes += 1

            self.split_child(n ,0)

            self.insert_nofull(n, key)
        else:
            self.insert_nofull(r, key)


    def __repr__(self):

        return "B-Tree: T= %d, height= %d, nodes= %d." % (self.t, self.height, self.nodes)

    def show_nodes(self):

        pass

    def inorder_walk(self):

        def inorder_walk_sub(x):
            if x.leaf:
                for i in xrange(0, x.n):
                    print x.keys[i],

                print "\n"
            else:

                for i in xrange(0, x.n):
                    inorder_walk_sub(x.children[i])
                    print x.keys[i]

                inorder_walk_sub(x.children[i + 1])

        inorder_walk_sub(self.root)

    def min(self, x = None):
        if x == None:
            x = self.root

        while (not x.leaf) and x.children[0] != None:
            x = x.children[0]

        return x.keys[0]

    def max(self, x = None):
        if x == None:
            x = self.root

        while (not x.leaf) and x.children[x.n] != None:
            x = x.children[x.n]

        return x.keys[x.n - 1]

    def predecessor(self, key):

        ((n, i), stack) = self.search(key)

        if n == None:
            return None

        if n.leaf:

            # key is in a leaf

            if i > 0:
                return n.keys[i - 1]
            else:
                p = stack[-1]
                del stack[-1]

                while p.children[0] == n and p != self.root:
                    n = p
                    p = stack[-1]
                    del stack[-1]

                if 1:
                    if p == self.root and p.children[0] == n:

                    # The following judgement is wrong, the above one is right
                    # if p == self.root:

                        # key is the min value
                        return None
                else:

                    # We can combine the ture case branch into the scan below
                    pass


                j = 0

                while j < p.n and p.keys[j] <= key:
                    j += 1
                return p.keys[j-1]
        else:

            # key is in a node

            return self.max(n.children[i])



    def successor(self, key):

        # Reverse procedure of predecessor.

        ((n, i), stack) = self.search(key)

        if n == None:
            return None

        if n.leaf:

            # key is in a leaf

            if i < n.n - 1:
                return n.keys[i+1]
            else:
                p = stack[-1]
                del stack[-1]

                while p.children[p.n] == n and p != self.root:
                    n = p
                    p = stack[-1]
                    del stack[-1]

                j = 0

                while j < p.n and p.keys[j] <= key:
                    j += 1
                return p.keys[j]
        else:

            # key is in a node

            return self.min(n.children[i+1])

    def combine_child(self, x, i):
        left = x.children[i]
        right = x.children[i+1]

        if __debug__:
            print "before combine_child: i", i
            print "before combine_child: x", x
            print "before combine_child: left", left
            print "before combine_child: right", right


        # Copy right into left
        left.keys[left.n] = x.keys[i]
        left.n += 1

        for j in xrange(0, right.n):
            left.keys[left.n + j] = right.keys[j]

        if not x.leaf:
            for j in xrange(0, right.n + 1):
                left.children[left.n + j] = right.children[j]

        left.n += right.n

        del right
        self.nodes -= 1

        # Modify necessary fields of x
        x.n -= 1

        for j in xrange(i, x.n):
            x.keys[j] = x.keys[j+1]

        for j in xrange(i + 1, x.n + 1):
            x.children[j] = x.children[j+1]

        x.keys[x.n] = None
        x.children[x.n + 1] = None

        if __debug__:
            print "after combine_child: i", i
            print "after combine_child: x", x
            print "after combine_child: left", left


    def delete(self, key, x = None):

        # More intutive way: search for the key, and split into 2 cases:
        # in a leaf and in a internal node, after solving the cases,
        # B-tree attributes could be violated upwards, we go back until
        # the root node to solve these violations.

        # A no-back-up way is described in CLRS textbook and implemented here.

        # Principle: Never back-up, must ensure that: x.n > t (1 more of the minimum)
        # The root of the child tree(subtree) must also have x.n > t and contain key.

        # The only exception is the root node, since the recursion start on root node,
        # we cannot ensure that root.n > t, if not, but pushing done the root key,
        # the root node could become empty, delete is and shrink the B-Tree height.

        if x == None:
            x = self.root

        if __debug__:
            print "delete key= ", key
            print x

        if not x.leaf:

            # Internal node

            i = 0
            while i < x.n and x.keys[i] < key:
                i += 1

            if x.keys[i] == key:

                left = x.children[i]
                right = x.children[i+1]

                if left.n >= self.t:
                    pre = self.max(left)
                    x.keys[i] = pre

                    self.delete(pre, left)
                else:
                    if right.n >= self.t:
                        suc = self.min(right)
                        x.keys[i] = suc

                        self.delete(suc, right)
                    else:
                        self.combine_child(x, i)

                        if x.n == 0:
                            # Only happens when x == root
                            self.root = left
                            del x
                            self.nodes -= 1
                            self.height -= 1
                        self.delete(key, left)
            else:
                next_node = x.children[i]

                if next_node.n >= self.t:
                    self.delete(key, next_node)
                else:

                    if i > 0:
                        left = x.children[i-1]
                    else:
                        left = None

                    if i < x.n - 1:
                        right = x.children[i+1]
                    else:
                        right = None

                    # Borrow one key from left sibling
                    if left != None and left.n >= self.t:
                        if __debug__:
                            print "before borrow frome left: "
                            print "x: ", x
                            print "next_node: ", next_node
                            print "left: ", left


                        next_node.n += 1

                        for j in xrange(next_node.n - 1, 0, -1):
                            next_node.keys[j] = next_node.keys[j-1]
                        for j in xrange(next_node.n, 0, -1):
                            next_node.children[j] = next_node.children[j-1]
                        next_node.keys[0] = x.keys[i-1]
                        next_node.children[0] = left.children[left.n]

                        x.keys[i-1] = left.keys[left.n-1]
                        left.keys[left.n-1] = None
                        left.children[left.n] = None
                        left.n -= 1

                        if __debug__:
                            print "after borrow frome left: "
                            print "x: ", x
                            print "next_node: ", next_node
                            print "left: ", left

                        self.delete(key, next_node)
                    else:
                        # Borrow one key from right sibling

                        if right != None and right.n >= self.t:
                            if __debug__:
                                print "before borrow frome right: "
                                print "x: ", x
                                print "next_node: ", next_node
                                print "right: ", right

                            next_node.n += 1
                            next_node.keys[next_node.n-1] = x.keys[i]
                            next_node.children[next_node.n] = right.children[0]
                            x.keys[i] = right.keys[0]

                            right.n -= 1
                            for j in xrange(0, right.n):
                                right.keys[j] = right.keys[j+1]
                            for j in xrange(0, right.n + 1):
                                right.children[j] = right.children[j+1]

                            right.keys[right.n] = None
                            right.children[right.n + 1] = None

                            if __debug__:
                                print "after borrow frome right: "
                                print "x: ", x
                                print "next_node: ", next_node
                                print "right: ", right

                            self.delete(key, next_node)
                        else:

                            # We can not borrow key from sibling, consider conbining children
                            if right != None:
                                self.combine_child(x, i)

                                if x.n == 0:
                                    # Only happens when x == root
                                    self.root = next_node
                                    del x
                                    self.nodes -= 1
                                    self.height -= 1

                                self.delete(key, next_node)
                            else:
                                self.combine_child(x, i-1)

                                if x.n == 0:
                                    # Only happens when x == root
                                    self.root = left
                                    del x
                                    self.height -= 1

                                self.delete(key, left)

        else:

            # x is a leaf

            for i in xrange(0, x.n):
                if x.keys[i] == key:
                    break

            x.n -= 1
            for j in xrange(i, x.n):
                x.keys[j] = x.keys[j+1]

def tests():

    T = BTree(2)
    keys = "FSQKCLHTVWMRNPABXYDZE"

    for key in keys:
        T.insert(key)

    print T

    T.inorder_walk()

    ((node, i), stack) = T.search('M')

    print "search M: "
    print "index i= %d" % i
    print node

    print stack

    ((node, i), stack) = T.search('E')

    print "search E: "
    print "index i= %d" % i
    print node

    print stack

    print "min: ", T.min()
    print "max: ", T.max()

    print "Predecessor of A: ", T.predecessor('A')
    print "Predecessor of C: ", T.predecessor('C')
    print "Predecessor of E: ", T.predecessor('E')
    print "Predecessor of M: ", T.predecessor('M')
    print "Predecessor of R: ", T.predecessor('R')
    print "Predecessor of K: ", T.predecessor('K')


    print "Successor of Z: ", T.successor('Z')
    print "Successor of A: ", T.successor('A')
    print "Successor of B: ", T.successor('B')
    print "Successor of H: ", T.successor('H')
    print "Successor of M: ", T.successor('M')

    print "Delete A: "
    T.delete('A')
    print T
    print T.root
    T.inorder_walk()

    print "Delete B: "
    T.delete('B')
    print T
    print T.root
    T.inorder_walk()

    print "Delete M: "
    T.delete('M')
    print T
    print T.root
    T.inorder_walk()
    T.inorder_walk()

    print "Delete Q: "
    T.delete('Q')
    print T
    print T.root
    T.inorder_walk()

    print "Delete K: "
    T.delete('K')
    print T
    print T.root
    T.inorder_walk()


if __name__ == "__main__":

    tests()
