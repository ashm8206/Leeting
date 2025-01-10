# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False

        curr_sum = 0
        def helper(root, curr_sum):
            if not root:
                return False
            
            curr_sum += root.val

            if root.left is None and root.right is None:
                return curr_sum==targetSum
            
            return helper(root.left, curr_sum) or helper(root.right, curr_sum)
        
        return helper(root, 0)
