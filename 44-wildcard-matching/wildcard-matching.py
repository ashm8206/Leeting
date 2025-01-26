class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # https://leetcode.com/problems/wildcard-matching/solutions/1336621/python-dfs-with-memoization-clean-concise/
        # @lru_cache()

        dp = {}
        def dfs(i, j):
            if j == len(p):
                return i == len(s)

            if i == len(s): 
                # end of string to match
                # then are the rest "*"
                return all(x == '*' for x in p[j:])
            
            if (i,j) in dp:
                return dp[(i,j)]

            if (s[i]==p[j] or p[j]=="?"):
                dp[(i,j)] = dfs(i+1,j+1)
                return dp[(i,j)]

            if p[j]=="*":
                dp[(i,j)] = dfs(i, j+1) or dfs(i+1, j)
                return dp[(i,j)]
            
            dp[(i,j)] = False
            return dp[(i,j)]
    
        return dfs(0,0)