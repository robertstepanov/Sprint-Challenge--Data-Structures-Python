"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from collections import deque


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree

    def insert(self, value):
        # check if the incoming value is greater than the current node's value
        if value >= self.value:
            # we know we need to go right
            # how do we know when we need to recurse again,
            # or when to stop?
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)
        else:
            value < self.value
        if self.left:
            self.left.insert(value)
        else:
            self.left = BSTNode(value)

        # CODE FROM LECTURE -------------------------------------------
        # if value < self.value:
        #      # we know we need to go left
        # #     # how do we know when we need to recurse again,
        # #     # or when to stop?
        #     if not self.left:
        #         # we can park our value here
        #         self.left = BSTNode(value)
        #     else:
        #         # we can't park here
        #         # keep searching
        #         self.left.insert(value)
        # else:
        #     # we know we need to go right
        #     if not self.right:
        #         self.right = BSTNode(value)
        #     else:
        #         self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # when we start searching, self will be the root
        # compare the target against self

        # Criteria for returning False: we know we need to go in one direction,
        # but there's nothing in the left or right direction
        if target == self.value:
            return True  # base case
        if target < self.value:
            # go left if left is a BSTNode
            # self.left is another node
            if not self.left:
                return False  # base case
            return self.left.contains(target)
        else:
            # go right if right is a BSTNode
            if not self.right:
                return False  # base case
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # we keep going right til no nodes remaining
        if not self.right:
            return self.value
        return self.right.get_max()
        # else:
        #     return self.right.get_max()

    def iterative_get_max(self):
        current_max = self.value

        current = self
        # traverse our structure
        while current is not None:
            if current.value > current_max:
                current_max = current.value
        # update our current_max variable if we see a larger value
            current = current.right
        return current_max

    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        # call the fn on the value at this node
        fn(self.value)
        # pass this function to left and right child
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)

    def iterative_for_each(self, fn):
        stack = []
        # add the root node
        stack.append(self)

        # loop so long as the stack still has elements
        while len(stack) > 0:
            current = stack.pop()
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

        fn(current.value)

    # Depth-First traversal
    # LIFO ordering of the tree elements

    # # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left is not None:
            node.left.in_order_print(node.left)
        if node.right is not None:
            node.right.in_order_print(node.right)
        # if node:

        #     self.in_order_print(self.left)

        #     self.in_order_print(self.right)
        # if not self:
        #     return
        # self.in_order_print(self.left)
        # self.in_order_print(self.right)

        # if not self:
        #     return
        # in_order_print(self.left)
        # in_order_print(self.right)

        # if self.left:
        #     self.left.in_order_print()

        # if self.right:
        #     self.right.in_order_print()

        # if node.left is not None:
        #     self.in_order_print(node.left)
        # print(node.value)
        # if node.right is not None:
        #     self.in_order_print(node.right)

        # Print the value of every node, starting with the given node,
        # in an iterative breadth first traversal

    def bft_print(self, fn):
        queue = deque()
        # add the root node
        queue.append(self)

        # loop so long as the queue still has elements
        while len(queue) > 0:
            current = queue.popleft()
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

            fn(current.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, fn):
        stack = []
        # add the root node
        stack.append(self)

        # loop so long as the stack still has elements
        while len(stack) > 0:
            current = stack.pop()
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

        fn(current.value)

    # # Stretch Goals -------------------------
    # # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
