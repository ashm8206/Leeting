# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):

        self.inorderOrder = []
        curr = root
        while curr:
            self.inorderOrder.append(curr)
            curr = curr.left
        # self.index = -1

        # def inorder(root):
        #     if not root:
        #         return 
        #     inorder(root.left)
        #     self.inorderOrder.append(root.val)
        #     inorder(root.right)
        # inorder(root)

    def next(self) -> int:
        topNode = self.inorderOrder.pop()
        curr = topNode.right

        # this can be move to a function
        while curr:
            self.inorderOrder.append(curr)
            curr = curr.left
        
        return topNode.val

        # self.index+=1
        # return self.inorderOrder[self.index]

    def hasNext(self) -> bool:
        # return self.index+1 < len(self.inorderOrder)
        return len(self.inorderOrder) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()