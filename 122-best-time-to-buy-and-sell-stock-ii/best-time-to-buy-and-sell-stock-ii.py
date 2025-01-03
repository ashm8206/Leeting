class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # profits =[ prices[i]-prices[i-1] for i in range(1,n)]

        # res = 0
        # for profit in profits:
        #     if profit > 0:
        #         res +=profit
        # return res

        # Time Complexity : O(N)
        # Space Complexity = O(N)

        #  Save Space

        res = 0

        for i in range(1, n):
            if prices[i] > prices[i-1]:
                res+= prices[i]-prices[i-1]
        return res