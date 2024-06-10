class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        # brute Force

        # #  hmap[s[R]] >= K

        # def atleastK(freq, k):

        #     for i in range(26):
        #         if freq[i]!=0 and freq[i] < k:
        #             return False
        #     return True

        

        # n = len(s)
        # maxLen = 0

        # for L in range(n):

        #     freq = [0]*26
        #     # set Zero freq for every substring
            
        #     for R in range(L, n):
        #         freq[ord(s[R]) - ord('a')]+=1

        #         if atleastK(freq, k):
        #             maxLen = max(maxLen, R-L+1)
        # return maxLen

        # for chars found in string
        # split on char that have freq[char] < k 
        for char, count in Counter(s).items():
            if count < k: 
                return max(self.longestSubstring(split_str, k) for split_str in s.split(char))
        return len(s)



