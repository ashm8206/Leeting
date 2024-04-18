# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # ABS(HL - HR) <= 1 @every node.
        # LRV
        def helper(root):

            if not root:
                return True, 0

            leftBalanced, leftHeight = helper(root.left)
            rightBalanced, rightHeight = helper(root.right)

            return leftBalanced and rightBalanced and abs(rightHeight-leftHeight) <=1, 1 + max(leftHeight,rightHeight)

        isBalanced, _  = helper(root)
        return isBalanced
            
            



        