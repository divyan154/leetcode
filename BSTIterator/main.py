class BSTIterator:
    def BSTIterator(self, root):
        self.__myStack = []
        self.pushAll(root)

    def hasNext(self):
        return len(self.__myStack) == 0 
    
    # returns the next smallest number   
    def next(self):
        tmpNode = self.__myStack.pop()
        self.pushAll(tmpNode.right)
        return tmpNode.val

    def __pushAll(self, root):
        while root != None:
            self.__myStack.append(root)
            root = root.left



# class TreeNode:
#     def TreeNode(self, root ):
#         self.root = root

