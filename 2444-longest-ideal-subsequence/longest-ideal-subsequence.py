class Solution:
    def longestIdealString(self, s: str, k: int) -> int:

        #  Method I - Vanilla LIS
        # ans = 1
        # n = len(s)
        # dp = [1 for i in range(n)]
        # maxLen = 1
        
        # for i in range(0,n):
        #     for j in range(0, i):
        #         if abs(ord(s[i]) - ord(s[j])) <= k:
        #             dp[i] = max(dp[i], dp[j]+1)
        #     maxLen = max(maxLen, dp[i])
        # # print(dp)
        # return maxLen

        maxLen = 1
        n = len(s)

        dp = [0 for i in range(26)] # longest ideal sequence for each [a-z]

        for i in range(n):

            curr = ord(s[i]) - ord('a')
            left = max(0, curr-k)
            right = min(25, curr+k)
            longest = 0
            for j in range(left, right+1):
                # for the valid adjacent strings:
                # what is the longest ideal sequence they have been part of?
                longest = max(longest, dp[j])
            dp[curr] = max(dp[curr], longest +1)
            maxLen = max(maxLen, dp[curr])
       
        return maxLen