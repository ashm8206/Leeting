# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = []
        def helper(root, path):
            if not root:
                return 

            path.append(str(root.val))
            if root.left is None and root.right is None:
                res.append(int("".join(path[:])))
                return 

            if root.left:
                helper(root.left,path)
                path.pop()

            if root.right:
                helper(root.right,path)
                path.pop()
        
        helper(root, [])
        return sum(res)
  
            
            