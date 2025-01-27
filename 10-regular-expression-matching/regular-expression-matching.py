class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # Option 1# https://leetcode.com/problems/regular-expression-matching/solutions/883719/python-top-down-dp-clean-concise-o-m-n/

        m, n = len(s), len(p)
        # @lru_cache()
        dp = {}
        def dfs(i, j):

            if j == n:
                return i == m

            if (i,j) in dp:
                return dp[(i,j)]
            
            match = i < m and (s[i] == p[j] or p[j] == ".")
            # use * only if prev is match
            # this condition can cause the pattern to keep growing
            # But we are only interested in  upto i < m

            if (j + 1) < n and p[j + 1] == "*":

                dp[(i,j)] = dfs(i, j+2) or (match and dfs(i + 1, j))

                # return (dfs(i, j + 2) or          # don't use * 
                #        (match and dfs(i + 1, j))) # use *
                # # use * only if prev is match
            
            elif match:
                dp[(i,j)] =  dfs(i + 1, j + 1)
            else:
                dp[(i,j)] = False
            
            return dp[(i,j)]
        
        dfs(0,0)
        return dp[(0,0)]
        