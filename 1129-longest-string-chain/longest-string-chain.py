class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        def isPredeccesor(word1, word2):
            m = len(word1)
            n = len(word2)

            if n-m > 1 or m==n:
                return False
            i = 0
            j = 0

            while i < m and j < n:
                if word1[i]== word2[j]:
                    i+=1
                    j+=1
                else:
                    j+=1
            # check to see if entire first word is completd
            # we may break if j... +++ keeps increasing
            return i == m
            
        
        result = 1
        n = len(words)
        words.sort(key = lambda x : len(x))

        dp = [ 1 for i in range(n)]

        for i in range(1, n):
            for j in range(0, i):
                #  if LIS condition
                if isPredeccesor(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j]+1)
            result = max(result, dp[i])
        return result