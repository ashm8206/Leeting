# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:     
        
        closest = 10**10
        while root:
            closest = min(closest, root.val, key = lambda x : (abs(x-target), x))
            # the key is tuple becuz if there are smaller values
            # we return the smallest value
            if target < root.val:
                root = root.left
            else:
                root = root.right
        
        return closest