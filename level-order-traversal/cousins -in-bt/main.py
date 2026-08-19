# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:


        q = []
        q.append(root)

        while q:
            sz = len(q)
            isAPresent = False
            isBPresent = False
            for _ in range(sz):
                node = q.pop(0)
                value = node.val

                if value == x :
                    isAPresent = True
                if value == y :
                    isBPresent = True

                if node.left and node.right:
                    if node.left.val == x and node.right.val == y:
                        return False
                    if node.left.val == y and node.right.val == x:
                        return False

                if isAPresent and isBPresent:
                    return True
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)        

        return False