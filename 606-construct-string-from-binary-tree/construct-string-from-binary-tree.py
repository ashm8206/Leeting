# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = []

        def preOrder(root):

            if not root:
                return
            
            res.append(str(root.val))

            if root.left:
                res.append('(')
                preOrder(root.left)
                res.append(')')

            if root.right:
                if root.left is None:
                    res.append('()')
                res.append('(')
                preOrder(root.right)
                res.append(')')
        
        preOrder(root)
        # print(res)
        return ''.join(res)