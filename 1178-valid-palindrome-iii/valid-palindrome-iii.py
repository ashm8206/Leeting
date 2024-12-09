class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        memo =  [[0 for j in range(n+1)] for i in range(n+1)]

        t = s[::-1]

        for i in range(1, n+1):
            for j in range(1,n+1):
                if s[i-1]==t[j-1]:
                    memo[i][j] = 1 + memo[i-1][j-1]
                else:
                    memo[i][j] = max(memo[i][j-1], memo[i-1][j])
        
    
   
        return n - memo[n][n] <= k