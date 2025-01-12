# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        
        # # Method I
        # if not root:
        #     return None

        # if p == root or q == root:
        #     return root # if we find either first, they are the LCA

        # left = self.lowestCommonAncestor(root.left, p, q)
        # right = self.lowestCommonAncestor(root.right, p, q)

        # if left and right: # split
        #     return root
        
        # return left or right # one of them comes before case II


        # Method II

        self.ans = None

        def helper(root, p, q): 

            if not root:
                return None, None

            pLeft, qLeft = helper(root.left, p, q)
            pRight, qRight = helper(root.right, p, q)

            pseen, qseen = False, False

            if pLeft or pRight or root == p:
                pseen = True
            
            if qLeft or qRight or root == q:
                qseen = True


            if pseen and qseen:
                if self.ans is None:
                    self.ans = root
            
            return pseen, qseen
    
        helper(root, p, q)
        
        return self.ans