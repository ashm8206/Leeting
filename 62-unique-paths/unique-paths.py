class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp = [[0] * n for _ in range(m)]
        # dp[0][0] = 1 # Base case
        

        # for row in range(m):
        #     for col in range(n):
        #         if row > 0:
        #             dp[row][col] += dp[row - 1][col]
        #         if col > 0:
        #             dp[row][col] += dp[row][col - 1]
        
        # return dp[m - 1][n - 1]

        0 # 0, 1
        1 # 1  2

        # Recursion
        # def helper(m,n):
        #     if m==0 or n==0:
        #         return 1
            

        #     return helper(m-1,n) + helper(m, n-1)
        # return helper(m-1,n-1)

        # Memoization
        cache = {}

        def helper(m,n):
            if m==0 or n==0:
                return 1
            
            if (m,n) in cache:
                return cache[(m,n)]
            
            cache[(m,n)] = helper(m-1,n) + helper(m, n-1)
            
            return cache[(m,n)]

        return helper(m-1,n-1)


        