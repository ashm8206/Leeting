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
        Sort by width ascending: Ensures when we process envelopes, all previous ones have smaller/equal width

Sort by height descending when widths are equal: Prevents choosing multiple envelopes with the same width
        '''
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        print(envelopes)
        tail = [] # on 2nd dimension
        for i in range(n):
            idx = bisect_left(tail, envelopes[i][1])
            if idx == len(tail):
                tail.append(envelopes[i][1])
            else:
                tail[idx] = envelopes[i][1]
            # print(tail)
        return len(tail)

       