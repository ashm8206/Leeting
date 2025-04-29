# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # def helper(root, low, high):
        #     # https://www.youtube.com/watch?v=s6ATEkipzow
        #     if not root:
        #         return True
            
        #     # if low < root.val < high:
        #     #     return True # Wrong this True depends on what the L and R subtree below would say
        #     # else:
        #     #     return False
        #     if root.val <= low or root.val>= high:
        #         return False
            
        #     return helper(root.left, low, root.val) and helper(root.right, root.val, high)
        
        # return helper(root,-2**32, 2**32)


        # def helper(root, leftSide, rightSide):

        #     if not root:
        #         return True
            
        #     if leftSide < root.val < rightSide:
        #         return helper(root.left, leftSide, root.val) and helper(root.right, root.val ,rightSide)
        #     return False

        # return helper(root, -2**31-1, 2**31+1)

        
        def helper(root, left, right):
            if not root:
                return True
            if root.val > left and root.val < right:
                return helper(root.left, left, root.val) and helper(root.right, root.val, right)
            else:
                return False
        return helper(root, float("-inf"), float("inf"))
        

    
            
        