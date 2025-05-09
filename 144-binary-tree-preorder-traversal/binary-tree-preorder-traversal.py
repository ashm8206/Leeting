# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []

        # def helper(root):
        #     if not root:
        #         return
        #     res.append(root.val)
        #     helper(root.left)
        #     helper(root.right)
        
        # helper(root)


        # Method II - stack

        if not root:
            return res

        stack = [root] #  keep state of what to pop next

        while stack:
            root = stack.pop()
            res.append(root.val)

            if root.right:
                stack.append(root.right)

            if root.left:
                stack.append(root.left)
            
        return res