class Solution:
    def shortestPalindrome(self, s: str) -> str:
        
        # Subproblem 1
        #find the longest Palindromic prefix : X
        # return substring X and its Start and End Position

        #final Problem
        # return reversed(S[R+1:N]) + X
        #  dc abacd

       

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
        
        return ""


      
