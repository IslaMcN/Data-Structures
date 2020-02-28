from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        node = BinarySearchTree(value)
        current = self
        while True:
            if value < current.value:
                if current.left == None:
                    current.left = node
                    return
                else:
                    current = current.left
            elif value > current.value:
                if current.right == None:
                    current.right = node
                    return
                else:
                    current = current.right
            

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        current = self
        while current is not None:
            if self.value == target:
                return True
            if target < current.value:
                if current.left:
                    return current.left.contains(target)
                else:
                    False
            elif target > current.value:
                if current.right:
                    return self.right.contains(target)
                else:
                    return False

        return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()
        
    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        if self.right != None and self.left != None:
            cb(self.value)
            self.left.for_each(cb)
            return self.right.for_each(cb)
        if self.right == None and self.left != None:
            cb(self.value)
            return self.left.for_each(cb)
        if self.right != None and self.left == None:
            cb(self.value)
            return self.right.for_each(cb)
        if self.right == None and self.left == None:
            cb(self.value)
            return

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        #Does node exist?
        if node == None:
            return
        #Print the data of node
        print(node.value)
        BinarySearchTree.in_order_print(self.left)
        BinarySearchTree.in_order_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass





