# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        self.dfs(root, p, q)
        return self.ans

    def dfs(self, node, p, q):
        if node is None:
            return False, False
        
        pleft, qleft = self.dfs(node.left, p, q)
        pright, qright = self.dfs(node.right, p, q)
        pseen = pleft or pright or node == p
        qseen = qleft or qright or node == q
        if pseen and qseen:
            if self.ans is None:
                self.ans = node
        return pseen, qseen