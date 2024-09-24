class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        R, C = len(matrix), len(matrix[0])
        cache = {}

        maxSqSide = float("-inf")
    
        def helper(r,c):

            nonlocal maxSqSide
            
            if r >= R or c >= C:
                return 0
            
            if (r,c) not in cache:
                cache[(r,c)] = 0
                down = helper(r+1,c)
                right = helper(r, c+1)
                diag = helper(r+1,c+1)
                if matrix[r][c] =='1':
                    
                    cache[(r,c)] = 1 + min(down,right, diag)
                
            maxSqSide = max(maxSqSide, cache[(r,c)])
            return cache[(r,c)]

        helper(0,0) 
        return maxSqSide * maxSqSide