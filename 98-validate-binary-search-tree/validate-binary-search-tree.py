# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(root, low, high):
            if not root:
                return True
            
            # if low < root.val < high:
            #     return True # Wrong this True depends on what the L and R subtree below would say
            # else:
            #     return False
            if root.val <= low or root.val>= high:
                return False
            
            return helper(root.left, low, root.val) and helper(root.right, root.val, high)
        
        return helper(root,-2**32, 2**32)
        