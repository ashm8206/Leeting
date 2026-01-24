# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        minNum = float("-inf")
        maxNum = float("inf")
        def helper(preorder, minNum, maxNum):
            if not preorder:
                return None
            
            root = None
            if minNum < preorder[0] < maxNum:
                parent = preorder.pop(0)
                root = TreeNode(parent)
                root.left =  helper(preorder, minNum, parent)
                root.right = helper(preorder, parent, maxNum)
            return root
        return helper(preorder, minNum, maxNum)
