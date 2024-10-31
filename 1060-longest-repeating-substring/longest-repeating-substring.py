class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        
        # n = len(s)
        # dp = [ [0  for j in range(n+1) ]  for i in range(n+1)]

        # maxLen = 0

        # for i in range(1, n+1):
        #     for j in range(1, n+1):

        #         if s[i-1]==s[j-1] and i!=j:
        #             dp[i][j] = 1 + dp[i-1][j-1]
        #             maxLen = max(maxLen, dp[i][j] )
        #         # else:
        #         # Not a subsequence, and no replacements allowed
        #         #     dp[i][j] = max( dp[i][j-1], dp[i-1][j])
        # return maxLen

        n = len(s)
        prev = [0  for j in range(n+1) ]

        maxLen = 0

        for i in range(1, n+1):
            curr = [0  for j in range(n+1) ]
            for j in range(1, n+1):
                if s[i-1]==s[j-1] and i!=j:
                    curr[j] = 1 + prev[j-1]
                    maxLen = max(maxLen, curr[j])
            prev = curr
        return maxLen
