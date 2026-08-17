# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root):

        if root == None:
            return 0

        lh = self.height(root.left)
        rh = self.height(root.right) 

        self.res = max(self.res, lh + rh)
        return 1 + max(lh,rh)   
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')
        self.height(root)
        return self.res

        