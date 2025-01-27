class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        dp  = {}
        def dfs(i, j):

            if j == len(p):
                return i == len(s)
            
            if (i,j) in dp:
                return dp[(i,j)]
            
            match = i < len(s) and (s[i]==p[j] or p[j]=="?")

            if match:
                dp[(i,j)] = dfs(i+1,j+1)

            elif p[j]=="*":
               
                dp[(i,j)]  =  dfs(i, j+1) or ( i < len(s) and dfs(i+1, j))             
            else:
                dp[(i,j)]= False
            
            return  dp[(i,j)]
    
        return dfs(0,0)

        # Memoization
        # https://leetcode.com/problems/wildcard-matching/solutions/1336621/python-dfs-with-memoization-clean-concise/
        @lru_cache()
        def dfs(i, j):
            if j == len(p):
                return i == len(s)

            # if i == len(s): 
            #     # end of string to match
            #     # then are the rest "*"
            #     return all(x == '*' for x in p[j:])
            

            if (i < len(s) and s[i]==p[j] or p[j]=="?"):
                return dfs(i+1,j+1)

            elif p[j]=="*":
                return dfs(i, j+1) or ( i < len(s) and dfs(i+1, j))

            else:
                return False
            
        return dfs(0,0)