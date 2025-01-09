class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        n = len(word1)
        m = len(word2)

        dp = {}
        def helper(i, j):
            if i>=n or j >=m:
                return 0

            if (i,j) in dp:
                return dp[(i,j)]
            
            if word1[i]==word2[j]:
                dp[(i,j)] =  1 + helper(i+1, j+1)
            else:
                dp[(i,j)] = max(helper(i+1, j), helper(i, j+1))

            return dp[(i,j)]
        
  
       
        return (m + n - 2*  helper(0, 0)) 



        # memo = [ [0 for j in range(n+1)] for i in range(m+1)]
        
        # for i in range(m+1):
        #     memo[i][0] = i
        
        # for j in range(n+1):
        #     memo[0][j] = j

        # for i in range(1, m+1):
        #     for j in range(1, n+1):
        #         if word1[i-1]==word2[j-1]:
        #             memo[i][j] = memo[i-1][j-1]
        #         else:
        #             memo[i][j] = 1 + min(memo[i-1][j], memo[i][j-1])
        # return memo[m][n]