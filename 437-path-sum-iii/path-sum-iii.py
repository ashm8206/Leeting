# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
        curr_sum = 0

        def computeSumInPath(root, curr_sum):
            nonlocal count
            if not root:
                return 0

            curr_sum += root.val

            if curr_sum == targetSum:
                count+=1
        
            computeSumInPath(root.left,curr_sum)
            computeSumInPath(root.right,curr_sum)
        
        
        def computeEachNode(root):
            if not root:
                return 
            computeSumInPath(root,0)
            computeEachNode(root.left)
            computeEachNode(root.right)


        computeEachNode(root)
        # Over all nodes it will check ComputeSumInPath

        return count