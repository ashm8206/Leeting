class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache()
        def dp(i,j):
            if j == len(p):
                return i == len(s)

            # preceeding logic first
            if j+1 < len(p) and p[j+1] == "*":
                # match preceeding 
                ans = dp(i, j+2) # matches zero j+2 j+1==*, skip these
                if i < len(s) and (s[i]==p[j] or p[j]=="."): 
                    ans = ans or dp(i+1,j)
                return ans
                    # skip 1 char in s, 
                    # don't skip in p since it can match 1 or more characters
            
            if i < len(s) and (s[i]==p[j]) or p[j]==".": 
                # match a single charac
                return dp(i+1,j+1)
            return False
        return dp(0,0)

