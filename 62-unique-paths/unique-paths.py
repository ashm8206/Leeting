class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 2*2 Mat

        0 # 0, 1
        1 # 1  2

        # Recursion
        # def helper(m,n):
        #     if m==0 or n==0:
        #         return 1
            

        #     return helper(m-1,n) + helper(m, n-1)
        # return helper(m-1,n-1)

        # Memoization
        # cache = {}

        # def helper(m,n):
        #     if m==0 or n==0:
        #         return 1
            
        #     if (m,n) in cache:
        #         return cache[(m,n)]
            
        #     cache[(m,n)] = helper(m-1,n) + helper(m, n-1)
            
        #     return cache[(m,n)]

        # return helper(m-1,n-1)

        # Tabulation

        dp = [ [ 0 for _ in range(n) ]for _ in range(m)]

        # Tricky bit, but only 1 way of reaching at start
        dp[0][0] = 1

        for row in range(m):
            for col in range(n):
                if row > 0:
                    # Top
                    dp[row][col] += dp[row-1][col] 
                if col > 0:
                    # Left to right
                    dp[row][col] += dp[row][col-1]
        return dp[m-1][n-1] 






        