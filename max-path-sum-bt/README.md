# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root : Optional[TreeNode]) -> int:
        if root == None:
            return 0

        leftPathSum =  max(0,self.dfs(root.left))
        rightPathSum = max(0,self.dfs(root.right))
        self.maxi = max(self.maxi, leftPathSum + rightPathSum + root.val)

        return (root.val + max(0,max(leftPathSum, rightPathSum)))



    def maxPathSum(self, root: Optional[TreeNode]) -> int:
      
        self.maxi = float('-inf')
        ans = self.dfs(root)
        return self.maxi
