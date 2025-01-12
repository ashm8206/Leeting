# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.ans = None

        def helper(root, p, q): 

            if not root:
                return None, None

            pseen, qseen = False, False

            if root==p:
                pseen = True
            
            if root == q:
                qseen = True

            pLeft, qLeft = helper(root.left, p, q)
            pRight, qRight = helper(root.right, p, q)

            if pLeft or pRight:
                pseen = True
            
            if qLeft or qRight:
                qseen = True

            
            # we can combine them^^

            # if pLeft or pRight or root == p:
            #     pseen = True
            
            # if qLeft or qRight or root == q:
            #     qseen = True


            if pseen and qseen:
                if self.ans is None:
                    self.ans = root
            
            return pseen, qseen
    
        helper(root, p, q)
        
        return self.ans

           




    #     self.ans = None
    #     self.dfs(root, p, q)
    #     return self.ans

    # def dfs(self, node, p, q):
    #     if node is None:
    #         return False, False
        
    #     pleft, qleft = self.dfs(node.left, p, q)
    #     pright, qright = self.dfs(node.right, p, q)

    #     pseen = pleft or pright or node == p
    #     qseen = qleft or qright or node == q
        
    #     if pseen and qseen:
    #         if self.ans is None:
    #             self.ans = node
    #     return pseen, qseen