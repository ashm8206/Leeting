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
            if  p is None and q is None:
                return True

            if p is None or q is None: #0 and 0
                return False 
        
            if p.val!=q.val:
                return False
        
            left = isSameTree(p.left, q.left)
            right = isSameTree(p.right, q.right)

            return left and right

           


        def checkEachNode(node):
            if node is None:
                return False

            # if node vals are same, then check if isSameTree

            elif node.val==subRoot.val and isSameTree(node,subRoot):
                # will only check once if you add it here 
                # isSameTree(node,subRoot) 
                #  instead and Return True if condition met 

                # else move on and try other children
                return True
            
            # check for their children
            else:
                return checkEachNode(node.left) or checkEachNode(node.right)
        
        return checkEachNode(root)