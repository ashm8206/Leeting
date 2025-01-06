class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        ans = s[0]
        maxLen = 1

        # odd length palindromes
        # chose a middle and expand in both direction
        for i in range(n):
            l, r = i, i
            while l >=0 and r < n and s[l] == s[r]:
                if r-l+1 > maxLen:
                    maxLen = r-l+1
                    ans = s[l:r+1]

                l-=1
                r+=1
            
            # even length palindrome
            # start with length 2 and expand in both directions

            l, r = i, i+1 # 2 len
            while l >=0 and r < n and s[l] == s[r]:
                if r-l+1 > maxLen:
                    maxLen = r-l+1
                    ans = s[l:r+1]
                l-=1
                r+=1
        return ans