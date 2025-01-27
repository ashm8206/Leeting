# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = -10**9
        # https://www.youtube.com/watch?v=Hr5cWUld4vU
        def gain_from_sub_tree(root):
            nonlocal maxSum
            if not root:
                return 0
            
            # # potential prune the -ve gain (Chose not to take them)
            # leftGain = max(gain_from_sub_tree(root.left),0)
            # rightGain = max(gain_from_sub_tree(root.right),0)
            
            leftGain = gain_from_sub_tree(root.left)
            rightGain = gain_from_sub_tree(root.right)
            

            maxSum = max(maxSum, max(leftGain,0) + max(rightGain,0) + root.val)

            # maxGain has to be reported
            # in Postorder 
            # the Root becomes the split position
            # as such only 1 split position is allowed
            # Split - Left and Right are both choosen
            return max(max(leftGain,0),  max(rightGain,0)) + root.val
        gain_from_sub_tree(root)
        return maxSum
        