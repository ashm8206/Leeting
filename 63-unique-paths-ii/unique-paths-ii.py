class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp =  [[0 for _ in range(m+1)] for _ in range(n+1)]

        

        if obstacleGrid[n-1][m-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        else:
            dp[n-1][m-1] = 1

        for row in range(n-1, -1, -1):
            for col in range(m-1, -1, -1):
                
                if obstacleGrid[row][col] == 1:
                    dp[row][col] = 0

                if obstacleGrid[row][col] == 0:
                    dp[row][col]+= (dp[row+1][col] + dp[row][col+1])
        return dp[0][0]

        # @lru_cache / Recursive
        # def helper(r,c):
        #     print(r,c)
        #     if r==0 or c==0 and obstacleGrid[r][c] == 0:
        #         return 1

        #     if r < 0 or c < 0 or obstacleGrid[r][c] == 1:
        #         return 0
            
        #     return helper(r-1, c) + helper(r, c-1)
           
        # return helper(n-1,m-1)
            
        