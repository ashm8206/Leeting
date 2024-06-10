class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        L = 0
        maxLen = 0

        for R in range(len(s)):

            if len(set(s[L:R+1])) > k:
                # print(s[L:R+1])
                L = L+1
            
            maxLen = max(maxLen, R-L+1)

        return maxLen