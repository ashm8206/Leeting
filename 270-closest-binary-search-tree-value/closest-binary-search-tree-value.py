# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:     
        
        closest = 10**10
        
        def helper(root):
            nonlocal closest
            if not root:
                return float("inf")

            closest = min(closest, root.val, key = lambda x: (abs(target-x),x))
            if target < root.val:
                return helper(root.left)
            else:
                return helper(root.right)
        helper(root)
        return closest


