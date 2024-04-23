# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        #Method I
        # if not root or p == root or q == root:
        #     return root

        # left = self.lowestCommonAncestor(root.left, p, q)
        # right = self.lowestCommonAncestor(root.right, p, q)

        # if left and right:
        #     return root
        
        # return left or right

        # Method II

        p_val = p.val
        q_val = q.val
        node = root

        while node:

            parent_val = node.val
            if p_val < parent_val and q_val < parent_val:
                node = node.left
            elif p_val > parent_val and q_val > parent_val:
                node = node.right
            else:
                return node
