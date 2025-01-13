class Solution:
    def longestPalindrome(self, s: str) -> str:

        maxLen = 0 
        n = len(s)
        
        longestString = ""
        for i in range(n):
            # odd Len
            l, r = i, i
            # print(i,s[i])
            while  r < n  and l >=0 and s[l]==s[r]:
                if r - l + 1 > maxLen:
                    maxLen = r - l + 1 
                    longestString = s[l:r+1]
                    # print(maxLen, s[l], s[r])
                l-=1
                r+=1
            
            # even
            l, r = i, i+1
            while  r < n  and l >=0 and  s[l]==s[r]:
                if r - l + 1 > maxLen:
                    maxLen = r - l + 1 
                    longestString = s[l:r+1]
                l-=1
                r+=1
        return longestString
        
        
            #even Len

        # n = len(s)
        # ans = s[0]
        # maxLen = 1

        # # odd length palindromes
        # # chose a middle and expand in both direction
        # for i in range(n):
        #     l, r = i, i
        #     while l >=0 and r < n and s[l] == s[r]:
        #         if r-l+1 > maxLen:
        #             maxLen = r-l+1
        #             ans = s[l:r+1]

        #         l-=1
        #         r+=1
            
        #     # even length palindrome
        #     # start with length 2 and expand in both directions

        #     l, r = i, i+1 # 2 len
        #     while l >=0 and r < n and s[l] == s[r]:
        #         if r-l+1 > maxLen:
        #             maxLen = r-l+1
        #             ans = s[l:r+1]
        #         l-=1
        #         r+=1
        # return ans