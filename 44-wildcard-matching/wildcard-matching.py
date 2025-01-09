class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # https://leetcode.com/problems/wildcard-matching/solutions/1336621/python-dfs-with-memoization-clean-concise/
        dp  = {}
        def dfs(i, j):

            if j == len(p):
                return i == len(s)
            
            if (i,j) in dp:
                return dp[(i,j)]
            
            if i < len(s) and (s[i]==p[j] or p[j]=="?"):
                dp[(i,j)] = dfs(i+1,j+1)
            
            if p[j]=="*":
               
                dp[(i,j)]  =  dfs(i, j+1) or ( i < len(s) and dfs(i+1, j))
              

            if (i,j) in dp and dp[(i,j)]:
                return True
            # if it  doesnt match return False
            dp[(i,j)]= False
            return  dp[(i,j)]
    
        return dfs(0,0)