class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxLen = -1
        n = len(s)
        if n < 1:
            return 0

        L  = 0
        window = ''

        for R in range(n):
            if s[R] not in window:
                window += s[R]
                maxLen = max(maxLen, len(window))
            else:
                
                L = window.index(s[R])
                window = window[L+1:] + s[R]
                
            # print(L,R)
        # print(s[L])
        # maxLen = max(maxLen, R - L + 1)
        return maxLen
            