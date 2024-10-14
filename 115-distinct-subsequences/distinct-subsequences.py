class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
       

        m = len(s)
        n = len(t)
        memo = {}

        def helper(i, j):

            if i==m or j==n or  m - i < n - j:
                return 1 if j==n else 0

            if (i,j) in memo:
                return memo[(i,j)]
          
            ans = helper(i+1,j)

            # print(ans)

            if s[i]==t[j]:
                ans += helper(i+1,j+1)

            memo[(i,j)] = ans

            return memo[(i,j)]

        return helper(0,0)
    
