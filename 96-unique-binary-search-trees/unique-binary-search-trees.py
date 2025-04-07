class Solution:
    def numTrees(self, n: int) -> int:
        
        memo = {}
        def helper(start, end):
            if start > end:
                return 1
            
            if (start,end) in memo:
                return memo[(start,end)]
            
            res = 0

            for i in range(start, end+1):
                leftTree = helper(start, i-1)
                rightTree = helper(i+1, end)
                res+= leftTree*rightTree
            memo[(start,end)] = res
            return res
        return helper(1, n)