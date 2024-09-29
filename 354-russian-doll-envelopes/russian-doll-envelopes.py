from bisect import bisect_left
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # envelopes.sort(key = lambda x : (x[0],x[1]), reverse = False)
 
        ans = 1

        n = len(envelopes)
        maxLen = 1

        #  Method I - LIS
        # dp = [1 for i in range(n)]
        # for i in range(1, n):
        #     for j in range(0, i):
        #         if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
        #             dp[i] = max(dp[i], dp[j]+1)
        #     maxLen = max(maxLen, dp[i])
     
        # return maxLen

        # Method II
        '''
        In order fix this, we don't just sort increasing in the first dimension - we also sort decreasing on the second dimension, so two envelopes that are equal in the first dimension can never be in the same increasing subsequence.
        '''
        envelopes.sort(key = lambda x: (x[0],-x[1]))
        tail = [] # on 2nd dimension
        for i in range(n):
            idx = bisect_left(tail, envelopes[i][1])
            if idx == len(tail):
                tail.append(envelopes[i][1])
            else:
                tail[idx] = envelopes[i][1]
        return len(tail)

       