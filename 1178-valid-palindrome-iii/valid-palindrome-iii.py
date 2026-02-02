class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:

        memo = {}
        i = 0
        j = len(s) - 1
        n = len(s)

        def helper(i, j):
            #  i <= j
            #  i > j break
            if i >=j:
                # single numbered are palindromes
                # if they cross each other return
                return 0

            if (i, j) in memo:
                return memo[(i, j)]
                
            if s[i] == s[j]:
                memo[(i, j)] = helper(i + 1, j - 1)
            else:
      
                memo[(i, j)] = 1 + min(helper(i + 1, j), helper(i, j - 1))

            return memo[(i, j)]

        ans = helper(i, j)
        return ans <= k

        # aaba

        # n = len(s)
        # memo =  [[0 for j in range(n+1)] for i in range(n+1)]

        # t = s[::-1]

        # for i in range(1, n+1):
        #     for j in range(1, n+1):
        #         if s[i-1]==t[j-1]:
        #             memo[i][j] = 1 + memo[i-1][j-1]
        #         else:
        #             memo[i][j] = max(memo[i][j-1], memo[i-1][j])

        # # #  TotalLen - LPS = Substitutions
        # return n - memo[n][n] <= k
