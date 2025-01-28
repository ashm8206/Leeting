class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # lcs with string and reverse string

        t = s[::-1]
        
        n = len(s)
        dp = [ [ 0 for j in range(n+1) ] for i in range(n+1)]

        
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                
                if s[i]==t[j]:

                    dp[i][j] = 1 + dp[i+1][j+1]

                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])

        return dp[0][0] 
                



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
