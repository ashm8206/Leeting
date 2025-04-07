# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        memo = {}
        def helper(start,end):

            res = []
            if start > end:
                res.append(None)
                return res
            if (start, end) in memo:
                return memo[(start, end)]
            
            for i in range(start, end+1):
                leftSubtree = helper(start, i-1)
                rightSubtree = helper(i+1, end)

                for left in leftSubtree:
                    for right in rightSubtree:
                        res.append(TreeNode(i, left=left, right=right))
            memo[(start, end)] = res
            return res
        return helper(1,n)

