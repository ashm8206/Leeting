class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # Memoization

        # @lru_cache(maxsize=None) # cache will grow indefiniely no entries evicted.
        # def helper(p1, p2):
        #     if p1 == len(text1) or p2 == len(text2):
        #         return 0
            
        #     if text1[p1]==text2[p2]:
        #         return 1 + helper(p1 +1, p2 + 1)
            
        #     else:
        #         return max(helper(p1 +1, p2), helper(p1, p2 + 1))

        # return helper(0,0)


        # Tabulation

        n = len(text1)
        m = len(text2)

        dp = [ [0 for j in range(n+1)]for i in range(m+1)]

     
        
        for i in range(m-1, -1, -1):
            for j in range(n-1,-1,-1):

                if text1[j]==text2[i]:
                    dp[i][j]= 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]

        
        # Space Optimized Tabulation

        n = len(text1)
        m = len(text2)

        prev = [0 for i in range(m+1)]
        
        for i in range(n-1,-1,-1):
            curr = [0 for i in range(m+1)]
            for j in range(m-1,-1,-1):

                if text1[i]==text2[j]:
                    curr[j] = 1 + prev[j+1]
                else:
                    curr[j] = max(prev[j+1], prev[j])
            prev = curr
        return prev[0]