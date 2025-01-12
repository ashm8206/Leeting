# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # # R, V, L
        # 8, 15, 21, 30, 
        # 3, 5, 6

        # val = R
        # root.val += val
        # root.left +=  root.val += val
        
        self.total = 0
        def helper(root):
            if not root:
                return
            helper(root.right)
            self.total+= root.val 
            root.val = self.total
            helper(root.left)
        helper(root)

        return root