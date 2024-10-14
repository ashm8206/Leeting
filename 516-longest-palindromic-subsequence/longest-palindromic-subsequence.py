class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # lcs with string and reverse string
        # s1 = s
        # s2 = s[::-1]
        # n = len(s)

        # dp = [[ -1 for j in range(n+1)] for i in range(n+1)]
        
        # for i in range(n+1):
        #     for j in range(n+1):

        #         if i==0 or j==0:
        #             dp[i][j] = 0
                
        #         if s1[i-1]==s2[j-1]:
        #             dp[i][j] = 1 + dp[i-1][j-1]
        #         else:
        #             dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        # return dp[n][n]
        s1 = s
        s2 = s[::-1]
        m = len(s1)
        n = len(s2)

        dp = [ [-1 for j in range(n+1)]for i in range(m+1)]

        for i in range(m+1):
            dp[i][0] = 0

        for j in range(n+1):
            dp[0][j] = 0

        
        for i in range(1,m+1):
            for j in range(1, n+1):

                if s1[i-1]==s2[j-1]:
                    dp[i][j]= 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        # Print LCS
        # lcs = []
        # i = m
        # j = n
        # while i > 0 and j > 0:
        #     # print(i-1, j-1)
        #     if s1[i-1]==s2[j-1]:
        #         lcs.append(s1[i-1])
        #         i-=1
        #         j-=1
            
        #     elif dp[i-1][j] > dp[i][j-1]:
        #         i-=1
        #     else:
        #         j-=1
        # print("".join(reversed(lcs)))
      
        return dp[m][n]
