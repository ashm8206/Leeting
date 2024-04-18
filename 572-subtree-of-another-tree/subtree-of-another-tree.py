# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(p,q):

            # if either are None, check if both are None
            if p is None or q is None: #0 and 0
                return p is None and q is None 
        
            if p.val!=q.val:
                return False
        
            left = isSameTree(p.left, q.left)
            right = isSameTree(p.right, q.right)

            return left and right

           


        def checkEachNode(node):
            if node is None:
                return False

            # elif root.val==subRoot.val:
            #     return isSameTree(root, subRoot)
            elif isSameTree(node,subRoot):
                return True
            
            else:
                return checkEachNode(node.left) or checkEachNode(node.right)
        
        return checkEachNode(root)