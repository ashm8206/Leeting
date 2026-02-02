class Solution:
    def isMatch(self, s: str, p: str) -> bool:


        n, m = len(s), len(p)


        dp = [[False for _ in range(m+1) ] for _ in range(n+1)]

        dp[0][0] = True
        # Base case: empty string with patterns 
        # like "a*", "a*b*", etc.

        for j in range(2, m + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
                
        for i in range(1, n+1):
            for j in range(1, m+1):
                
                if p[j-1] == "*":
                    
                    match_with_start = s[i-1]==p[j-2] or p[j-2]=="."

                    dp[i][j] = dp[i][j-2] or (match_with_start and dp[i-1][j])
                
                elif s[i-1]==p[j-1] or p[j-1]==".":

                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = False
        
        return dp[n][m]

        dp = {}
        def dfs(i, j):

            if j == m:
                return i == n

            if (i,j) in dp:
                return dp[(i,j)]

            
            match = i < n and (s[i] == p[j] or p[j] == ".")

            #  p= a* s = aa
            # check * before direct match
            
            if (j + 1) < m and p[j + 1] == "*":
                #  Pre-check if next char is "*"
                # matches 0, so skip j and j + 1
                # pass j + 2 as next valid

                dp[(i,j)] = dfs(i, j+2) or ( # Match zero
                    # Match 1 and mored
                    match and dfs(i + 1, j)
                )

            elif match:
                dp[(i,j)] = dfs(i+1,j+1)
            else:
                dp[(i,j)] =  False
            
           

            # if (j + 1) < n and p[j + 1] == "*":
            #     # j+1= "*", so start at j+2
            #     dp[(i,j)] = dfs(i, j+2) 
            # or 
            #    (match and dfs(i + 1, j))
            #     # zero match or match 1 more of preceeding 
            #     # match current and send (i+1, j )  i+1 with same j
           
            
            return dp[(i,j)]
        
        dfs(0,0)
        return dp[(0,0)]



        # Memoized implicit


        # Option 1# https://leetcode.com/problems/regular-expression-matching/solutions/883719/python-top-down-dp-clean-concise-o-m-n/

        # m, n = len(s), len(p)
        # @lru_cache()
        # def dfs(i, j):
        #     if j == n:
        #         return i == m
            
        #     match = i < m and (s[i] == p[j] or p[j] == ".")
        #     # use * only if prev is match
        #     # this condition can cause the pattern to keep growing
        #     # But we are only interested in  upto i < m

        #     if (j + 1) < n and p[j + 1] == "*":
        #         return (dfs(i, j + 2) or          # don't use * 
        #                (match and dfs(i + 1, j))) # use *
        #         # use * only if prev is match
        #     if match:
        #         return dfs(i + 1, j + 1)
        #     return False
        
        # return dfs(0, 0)
        