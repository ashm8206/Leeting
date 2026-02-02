class Solution:
    def isMatch(self, s: str, p: str) -> bool:


        m, n = len(s), len(p)
        
        # dp[i][j] = whether s[0:i] matches p[0:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Base case: empty string matches empty pattern
        dp[0][0] = True
        
        # Base case: empty string can match pattern with only '*'
        for j in range(1, n + 1):
            # for any * in pattern
            # for first row in str1 , ""
            if p[j - 1] == '*':
                # save in this position, what was in prev pos
                dp[0][j] = dp[0][j - 1]

        # print(dp)
    #       ""      *
    #  ""  [[True, True], 
    #   a  [False, False], 
    #   a  [False, False]]
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # '*' matches 0 chars OR 1+ chars
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    # Characters match
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # No match
                    dp[i][j] = False
        
        return dp[m][n]
        
        # dp  = {}
        # def dfs(i, j):

        #     # Both exhausted → match
        #     if i == len(s) and j == len(p):
        #         return True
            
        #     # Pattern exhausted, string not → no match
        #     if j == len(p):
        #         return False
        
        #     # String exhausted, pattern not 
        #     # → only match if remaining are all '*'
        #     if i == len(s):
        #         return all(c == '*' for c in p[j:])
            
        #     if j == len(p):
        #         return i == len(s)
            
           
            
        #     if (i,j) in dp:
        #         return dp[(i,j)]
            
        #     match = s[i]==p[j] or p[j]=="?"

        #     if match:
        #         dp[(i,j)] = dfs(i+1,j+1)

        #     elif p[j]=="*":
               
        #         dp[(i,j)]  =  dfs(i, j+1) or  dfs(i+1, j)      
        #     else:
        #         dp[(i,j)]= False
            
        #     return  dp[(i,j)]
    
        # return dfs(0,0)

     

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