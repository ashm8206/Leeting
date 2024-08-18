class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp =  [[0 for _ in range(m)] for _ in range(n)]

        

        if obstacleGrid[0][0] == 1:
            return 0
        else:
            dp[0][0] = 1

        for row in range(n):
            for col in range(m):
                
                if obstacleGrid[row][col] == 1:
                    dp[row][col] = 0

                if row > 0 and obstacleGrid[row][col] == 0:
                    dp[row][col]+= dp[row-1][col]

                if col > 0 and obstacleGrid[row][col] == 0:
                    dp[row][col]+= dp[row][col-1]
        
        return dp[n-1][m-1]
        # @lru_cache / Recursive
        # def helper(r,c):
        #     print(r,c)
        #     if r==0 or c==0 and obstacleGrid[r][c] == 0:
        #         return 1

        #     if r < 0 or c < 0 or obstacleGrid[r][c] == 1:
        #         return 0
            
        #     return helper(r-1, c) + helper(r, c-1)
           
        # return helper(n-1,m-1)
            
        