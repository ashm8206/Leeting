# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        
        if l == 0:
            return 1 + r
        elif r == 0:
            return 1 + l
        return 1 + min(l, r)
        

       # Python3
# class Solution:
#     def minDepth(self, root):
#         # Define the depth-first search
#         def dfs(root):
#             if root is None:
#                 return 0
#             # If only one of child is non-null, then go into that recursion.
#             if root.left is None:
#                 return 1 + dfs(root.right)
#             elif root.right is None:
#                 return 1 + dfs(root.left)
#             # Both children are non-null, hence call for both children.
#             return 1 + min(dfs(root.left), dfs(root.right))

#         return dfs(root)
