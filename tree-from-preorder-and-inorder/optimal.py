# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build(self, preorder : deque, mapping, start, end):

        if start <= end:
            root_val = preorder.popleft()
            node = TreeNode(root_val)
            idx = mapping[root_val]

            node.left = self.build(preorder, mapping, start, idx - 1)
            node.right = self.build(preorder, mapping, idx + 1, end)
            return node
        return None    





    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        preorder = deque(preorder)
        
        mapping = {}
        for i in range(n):
            mapping[inorder[i]] = i

        return self.build(preorder, mapping, 0, n - 1)

# time complexity - 0(N) 
# Space complexity - 0(N) HashMap lookup
        