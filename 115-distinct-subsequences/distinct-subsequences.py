class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
       
        n = len(s)
        m = len(t)
        dp = {}

        def helper(i,j):
            if i == n or j == m:
                return 1  if j==m else 0
            
            
            if (i,j) in dp :
                return dp[(i,j)]

            res = helper(i+1, j)
            if s[i]==t[j]:
                res += helper(i+1, j+1)
            dp[(i,j)] = res
            return dp[(i,j)]
            
        return helper(0,0)

        # m = len(s)
        # n = len(t)
        # memo = {}

        # def helper(i, j):

        #     if i==m or j==n or  m - i < n - j:
        #         return 1 if j==n else 0

        #     if (i,j) in memo:
        #         return memo[(i,j)]
          
        #     ans = helper(i+1,j)

        #     # print(ans)

        #     if s[i]==t[j]:
        #         ans += helper(i+1,j+1)

        #     memo[(i,j)] = ans

        #     return memo[(i,j)]

        # return helper(0,0)
    
