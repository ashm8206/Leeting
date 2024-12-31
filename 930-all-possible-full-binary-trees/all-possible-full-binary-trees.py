
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        
        # allFBT(7)
        # # 0, 6. 1, 5 2, 4 3, 3 4, 2 5, 1, 6,0
        # what happens for 2 ?  or 4 or 6 ? -> []

        dp = {}

        def helper(n):
            # base case:
            if n%2==0:
                return []
            if n==1:
                return [TreeNode(0)]

            if n in dp:
                return dp[n]

            res = []

            for l in range(1, n, 2):
                r = n - 1 - l
                leftTrees, rightTrees = helper(l), helper(r)
                
                
                for left in leftTrees:
                    for right in rightTrees:
                        root = TreeNode(0, left=left, right=right)
                        res.append(root)
            dp[n] = res
            return res

        return helper(n)
