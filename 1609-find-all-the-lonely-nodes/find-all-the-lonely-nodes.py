# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def helper(node):
            if not node:
                return
            
            if (node.left and not node.right):
                res.append(node.left.val)

            if (node.right and not node.left):
                res.append(node.right.val)
            helper(node.left)
            helper(node.right)

        helper(root)
        return res