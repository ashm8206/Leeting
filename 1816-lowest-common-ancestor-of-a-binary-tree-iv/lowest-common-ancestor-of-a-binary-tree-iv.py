# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nodes = set(nodes)
        def dfs(node):
            if not node or node in nodes:
                return node

            lsub= dfs(node.left)
            rsub= dfs(node.right)

            if lsub and rsub:
                return node
            return lsub or rsub
        return dfs(root)