class Solution:
    def shortestPalindrome(self, s: str) -> str:
        
        # Subproblem 1
        #find the longest Palindromic prefix : X
        # return substring X and its Start and End Position

        #final Problem
        # return reversed(S[R+1:N]) + X
        #  dc abacd

        # if not s:
        #     return ""
            
        # def isPalindrome(s, end):
        #     # Check if s[0:end+1] is a palindrome
        #     i, j = 0, end
        #     while i < j:
        #         if s[i] != s[j]:
        #             return False
        #         i += 1
        #         j -= 1
        #     return True
        
        # # Find the longest palindromic prefix
        # n = len(s)
        # longest_pal = 0
        
        # # Try each position as potential end of palindromic prefix
        # for i in range(n-1, -1, -1):
        #     if isPalindrome(s, i):
        #         longest_pal = i
        #         break
        
        # return s[longest_pal + 1:][::-1] + s

        if not s:
            return ""
        
        # Get original string and its reverse
        rev = s[::-1]
        new_s = s
        
        # Find the longest palindromic prefix by checking if truncated 
        # reversed string exists at the start of original string
        for i in range(len(s)):
            if s.startswith(rev[i:]):
                return rev[:i] + s
        
        return rev + s[1:]


      
