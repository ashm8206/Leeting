class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:



        n, m = len(grid), len(grid[0])

        #optimized

            
        for  j in range(1,m):
            grid[0][j] += grid[0][j-1]

        for  i in range(1,n):
            grid[i][0] += grid[i-1][0]

       
    
        for i in range(1,n):
            for j in range(1,m):
            
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
            
        
        return grid[n-1][m-1]

        
        # dp = [[grid[i][j] for j in range(m)] for i in range(n)]

        # for i in range(n):
        #     for j in range(m):
                
        #         if i==0 and j > 0:
        #             dp[i][j] += dp[i][j-1] # remember dp[i][j] will have cost already

        #         elif j==0 and i > 0:
        #             dp[i][j] += dp[i-1][j]
                
        #         elif i > 0 and j > 0:
        #             dp[i][j] += min(dp[i-1][j],dp[i][j-1])
                
        
        # #print(dp)
        # return dp[n-1][m-1]
            


        