# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        #Method I
        if not root or p == root or q == root:
            return root

        left = None
        right = None
        if  p.val < root.val and  q.val < root.val:
            left = self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            right = self.lowestCommonAncestor(root.right, p, q)
        
        else:
            return root

        return left or right




        # Method II

        curr = root

        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif (p.val >= curr.val and q.val <= curr.val) or (p.val <= curr.val and q.val >= curr.val):
                return curr

                # if p < curr and curr > q we found a split
                # but its possible that p==curr or q>=q
                # p=2, q=6, in this case 6 is the LCA
        return None