class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        n = len(s)

        if n >= 2 and s == s[::-1]:
            return True

        reversed_s = s[::-1]
        for i in range(n-2+1):
            window = s[i:i+2]
            if window in reversed_s:
                return True
        return False

        # leafbcaef # fails
     


        