# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        unival_left =  self.isUnivalTree(root.left)
        unival_right = self.isUnivalTree(root.right)

        if unival_left and unival_right:
            if (not root.left or root.left and root.left.val == root.val) and (not root.right or root.right and root.right.val == root.val):
                return True
        return False