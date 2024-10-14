class Solution:
    def longestPalindrome(self, s: str) -> str:
        r = s[::-1]
        n = len(s)
        # Tabulation
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        max_length = 0
        max_end = 0
        
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                # Storing longest common substring in dp Array
                if s[i - 1] == r[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                # Code to check i and j
                if dp[i][j] > max_length:
                    if i - dp[i][j] == len(s) - j:
                        max_length = dp[i][j]
                        max_end = i
        return s[max_end - max_length:max_end]