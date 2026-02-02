class Solution:
    def isMatch(self, s: str, p: str) -> bool:


        m, n = len(s), len(p)

        dp = {}
        def dfs(i, j):

            if j == n:
                return i == m

            if (i,j) in dp:
                return dp[(i,j)]

            
            match = i < m and (s[i] == p[j] or p[j] == ".")

            #  p= a* s = aa
            # check * before direct match
            
            if (j + 1) < n and p[j + 1] == "*":
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
        