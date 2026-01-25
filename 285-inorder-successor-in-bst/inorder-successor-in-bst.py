# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        if root is None:
            return None
        
        
        # smallest value in greater than this node
        # node in Left of Root: that value is the closest root
        # node in right of Root:  thta is the next right child
        
        successor = None
        while root:
            if p.val < root.val:
                successor = root # potentially
                root = root.left
            else: #p.val >=root.val 
                root = root.right
        return successor
             