class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # https://leetcode.com/problems/wildcard-matching/solutions/1336621/python-dfs-with-memoization-clean-concise/
        @lru_cache()
        def dfs(i, j):
            if j == len(p):
                return i == len(s)
            
            if i < len(s) and (s[i]==p[j] or p[j]=="?"):
                return dfs(i+1,j+1)
            
            if p[j]=="*":
                return dfs(i, j+1) or ( i < len(s) and dfs(i+1, j))

            return False
    
        return dfs(0,0)