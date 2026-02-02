class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # lcs with string and reverse string

        n = len(s)
        dp = [ [ 0 for j in range(n+1) ] for i in range(n+1)]

        t = s[::-1]
        for i in range(1, n+1):
            for j in range(1, n+1):
                
                if s[i-1]==t[j-1]:

                    dp[i][j] = 1 + dp[i-1][j-1]

                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[n][n] 

        # method II 
        # n = len(s)
        # dp = [ [ 0 for j in range(n) ] for i in range(n)]

        
        # for i in range(n-1, -1, -1):
        #     dp[i][i] = 1
        #     for j in range(i+1, n):
                
        #         if s[i]==s[j]:

        #             dp[i][j] = dp[i+1][j-1] + 2

        #         else:
        #             dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        # return dp[0][n-1] 


        
                



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
      
        # return dp[m][n]
