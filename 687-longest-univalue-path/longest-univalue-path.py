# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        max_length = 0
        
        def dfs(node):
            nonlocal max_length
            if not node:
                return 0
            
            left_length = dfs(node.left)   # univalued path
            right_length = dfs(node.right) # univalued path

            left_arrow = right_arrow = 0

            # if there parent!=node there is no path to increm
            # assign two values and check condition

            if node.left and node.left.val == node.val:
                left_arrow = left_length + 1
            if node.right and node.right.val == node.val:
                right_arrow = right_length + 1

            # Max_lenght calcu through every node, where node is curr_node

            # But it can go to parent or grandparent and find that they are not equal
            # in That case you have to reset
            
            max_length = max(max_length, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)
        
        dfs(root)
        return max_length
