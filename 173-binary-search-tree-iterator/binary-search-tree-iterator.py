# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):

        self.inorderOrder = []
        self.next_left(root)
   
    def next_left(self, node):
        while node:
            self.inorderOrder.append(node)
            node = node.left


    def next(self) -> int:
        topNode = self.inorderOrder.pop()
        node = topNode.right
        self.next_left(node)
        return topNode.val

    def hasNext(self) -> bool:
        # return self.index+1 < len(self.inorderOrder)
        return len(self.inorderOrder) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()