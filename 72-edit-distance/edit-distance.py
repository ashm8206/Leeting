class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        m = len(word1)
        n = len(word2)
        memo = {}

        def helper(s1, s2, m, n):
            if m<0:
                return n
            if n<0:
                return m
            
            if (m, n) in memo:
                return memo[(m, n)]
            
            if s1[m]==s2[n]:
                return helper(s1,s2,m-1,n-1)
            
            else:
                memo[(m, n)] = 1 +  min(helper(s1,s2,m,n-1),helper(s1,s2,m-1,n), helper(s1,s2,m-1,n-1))
           
            return memo[(m, n)]
        
        return 1 + helper(word1,word2, m-1, n-1)
