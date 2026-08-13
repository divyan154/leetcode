'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''
from queue import Queue
from collections import deque, defaultdict
class Solution:
    def bottomView(self, root):
        """
        Function to return the
        bottom view of the binary tree
        """
        # Vector to store the result
        ans = []

        # Check if the tree is empty
        if root is None:
            return ans

        # Map to store the bottom view nodes
        # based on their vertical positions
        mpp = defaultdict(int)

        # Queue for BFS traversal, each
        # element is a pair containing node
        # and its vertical position
        q = Queue()

        # Push the root node with its vertical
        # position (0) into the queue
        q.put((root, 0))

        # BFS traversal
        while not q.empty():
            # Retrieve the node and its vertical
            # position from the front of the queue
            it = q.get()
            node, line = it[0], it[1]

            # Update the map with the node's data
            # for the current vertical position
            mpp[line] = node.data

            # Process left child
            if node.left:
                # Push the left child with a decreased
                # vertical position into the queue
                q.put((node.left, line - 1))

            # Process right child
            if node.right:
                # Push the right child with an increased
                # vertical position into the queue
                q.put((node.right, line + 1))

        # Transfer values from the
        # map to the result vector
        for key, value in sorted(mpp.items()):
            ans.append(value)

        return ans
        