# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        
        # firstMin = float(10**9)  
        # secondMin = float(10**9)

        res = [float(2**32), float(2**32)]
        def helper(root):
            # nonlocal firstMin
            # nonlocal secondMin
            
            firstMin, secondMin = res
            # print(firstMin, secondMin)
            if not root:
                return 
            if root.val < firstMin:
                secondMin = firstMin
                firstMin = root.val
            elif root.val < secondMin and root.val > firstMin:
                secondMin = root.val

            res[0] = firstMin
            res[1] = secondMin

            helper(root.left)
            helper(root.right)
             
        helper(root)
        return res[1] if res[1] < 2**32 else -1