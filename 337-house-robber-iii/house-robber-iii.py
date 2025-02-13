# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def helper(root):

            if not root:
                return (0,0) #[rob, dont_rob]
            
            left = helper(root.left) # returns a tuple
            right = helper(root.right)

            withRoot =  root.val + left[1] + right[1] 
            #index[1] = without children
            withoutRoot = max(left) + max(right)
            # ^^either of the values

            return (withRoot,withoutRoot)
        
        return max(helper(root))
            
