import bisect
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        # # Method I
        # pairs.sort(key = lambda x: x[0])
      
        # lastEnd = pairs[0][1]
        # n = len(pairs)
        # ans = 1
        # for start, end in pairs:
        #     if start > lastEnd:
        #         ans += 1
        #         lastEnd = end
        #     else:
        #         lastEnd = min(lastEnd, end)
            
        # return ans

        # Method II

        pairs.sort()
        n = len(pairs)
        dp = [1 for i in range(n)]
        maxLen = 1

        for i in range(1, n):
            for j in range(0, i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j]+1)
            maxLen = max(maxLen, dp[i])
     
        return maxLen