# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:

        count = 0
        def helper(root):
            nonlocal count
            if not root:
                return 0, 0 # val, count

            leftSum, leftCount = helper(root.left)
            rightSum, rightCount = helper(root.right)


            average = math.floor((leftSum+rightSum+root.val)//(leftCount+rightCount+1))
            
            if average == root.val:
                count+=1
            
            return root.val + leftSum + rightSum, 1 + leftCount + rightCount
        
        helper(root)
        return count


        