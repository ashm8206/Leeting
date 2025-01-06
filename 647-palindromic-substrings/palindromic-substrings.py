class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        # odd length palindromes
        # chose a middle and expand in both direction
        for i in range(n):
            l, r = i, i
            while l >=0 and r < n and s[l] == s[r]:
                count+=1
                l-=1
                r+=1
            
            # even length palindrome
            # start with length 2 and expand in both directions

            l, r = i, i+1 # 2 len
            while l >=0 and r < n and s[l] == s[r]:
                count+=1
                l-=1
                r+=1
        return count
            
    





       