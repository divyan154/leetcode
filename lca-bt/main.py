# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, root , p, q) -> 'TreeNode':
        if root == None or root == p or root == q:
            return root

        left =  self.dfs(root.left, p, q)
        right = self.dfs(root.right, p , q)
        
        val = False
        # Result
        if left is None:
            return right
        elif right is None:
            return left
        else: # Both left and right are not null, we found our result
            return root
     
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.dfs(root, p , q)

# Time complexity - 0(N)
# Space - 0(1) Stack Space 0(logn) in case of balanced bt otherwise 0(N) in case of skewed Tree