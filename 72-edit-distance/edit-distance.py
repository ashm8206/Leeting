class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        # m = len(word1)
        # n = len(word2)
        # memo = {}

        # def helper(s1, s2, m, n):
        #     if m ==0:
        #         return n # number of remaining characters in word2
        #     if n==0:
        #         return m
            
        #     if (m, n) in memo:
            
        #         return memo[(m, n)]

        #     print(memo, print(m,n))

        #     if s1[m-1]==s2[n-1]:
        #         return helper(s1,s2,m-1,n-1)

        #     else:
        #         memo[(m, n)] = 1 +  min(helper(s1,s2,m,n-1),helper(s1,s2,m-1,n), helper(s1,s2,m-1,n-1))
            
        #     return memo[(m, n)]
        
        # return helper(word1,word2, m, n)

        # you are missing the comparsion for ("" "") and missing hence the result will be off By 1
        

    
        # m = len(word1)
        # n = len(word2)
        # memo = {}

        # def helper(s1, s2, m, n):

        #     if m <= -1:
        #         return n + 1
        #     if n <= -1:
        #         return m + 1
            
        #     if (m, n) in memo:
            
        #         return memo[(m, n)]

        #     print(memo, print(m,n))

        #     if s1[m]==s2[n]:
        #         return helper(s1,s2,m-1,n-1)

        #     else:
        #         memo[(m, n)] = 1 +  min(helper(s1,s2,m,n-1),helper(s1,s2,m-1,n), helper(s1,s2,m-1,n-1))
            
        #     return memo[(m, n)]
        
        # return helper(word1,word2, m-1, n-1)

        m = len(word1)
        n = len(word2)

        memo = [ [-1 for j in range(n+1)] for i in range(m+1)]
        for i in range(m+1):
            memo[i][0] = i
        
        for j in range(n+1):
            memo[0][j] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1]==word2[j-1]:
                    memo[i][j] = memo[i-1][j-1]
                else:
                    memo[i][j] = 1 + min(memo[i-1][j], memo[i][j-1], memo[i-1][j-1])
        return memo[m][n]