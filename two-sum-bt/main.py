# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root : Optional[TreeNode], isReverse : bool):
        self.__myStack = []
        self.reverse = isReverse
        self.__pushAll(root)
        # reverse == true --- before
        # reverse == False  --- next

    def hasNext(self):
        return len(self.__myStack) != 0

    def next(self):
        tmpNode = self.__myStack.pop()
        if self.reverse == False:
            self.__pushAll(tmpNode.right)
        else:
            self.__pushAll(tmpNode.left)
        return tmpNode.val

    def __pushAll(self, root):   
        while root != None:
            self.__myStack.append(root)

            if self.reverse == False:
                root = root.left
            else:
                root = root.right    





class Solution:

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        l = BSTIterator(root, False)
        r = BSTIterator(root, True)
        
        i = l.next()
        j = r.next()

        while i < j:
            if i + j == k:
                return True
            elif i + j < k:
                i = l.next()
            else:
                j = r.next()        

        return False        