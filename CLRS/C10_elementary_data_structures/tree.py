#!/usr/bin/env python

# Since we only deal with how to print a tree, but no assumptions
# about how to insert and delete node. So, the algorithms here
# is much like pseudo codes.

class BinaryTreeNode:
    def __init__(self, key, parent, left = None, right = None):
        self.key = key
        self.parent = parent # This is needed by PrintBinaryTree3
        self.left = left
        self.right = right

# Recursive

def PrintBinaryTree(root):
    if root == None:
        return
    else:
        print root.key
        PrintTree(root.left)
        PrintTree(root.right)


# Nonrecursive, with a stack as helper

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

def PrintBinaryTree2(root):
    if root == None:
        return

    node = root
    s = BlackBoxStack()

    while True:
        print node.key

        if node.right != None:
            s.push(node.right)

        if node.left == None:
            if s.is_empty():
                break;
            else:
                node = s.pop()
        else:
            node = node.left


# Nonrecursive, with constant extra space

# This is tricky. We need a pointer to the parent. We keep track of the previous pointer (starting with NIL) and do the following.

# If we're coming from the parent, move to the left child
# If we're coming from the left child, move to the right child
# If we're coming from the right child, move to the parent

def PrintBinaryTree3(node):
    prev = None
    while node is not None:
        if node.parent == prev:
            print node.key
            prev = node
            if node.left is None:
                node = node.parent
            else:
                node = node.left
        elif node.left == prev:
            prev = node
            if node.right is None:
                node = node.parent
            else:
                node = node.right
        else:
            prev = node
            node = node.parent

# Unbounded branching tree

class TreeNode:
    def __init__(self, key, parent, left_child = None, right_sibling = None):
        self.key = key
        self.parent = parent
        self.left_child = left_child
        self.right_sibling = right_sibling

# Recursive

def PrintUnboundedTree(root):
    if root == None:
        return
    else:
        print root.key
        child = root.left_child

        while child != None:
            if child.left_child != None:
                PrintUnboundedTree(child)
            else:
                print child.key
                child = child.right_sibling
