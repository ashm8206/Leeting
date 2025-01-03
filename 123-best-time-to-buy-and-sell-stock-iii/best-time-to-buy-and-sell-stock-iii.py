class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # find largest in One transaction
        # minPrice = float("inf")
        # ans = 0
        # n = len(prices)

        # for j in range(1,n):
        #     minPrice = min(minPrice,prices[j-1])
        #     ans = max(ans, prices[j] - minPrice)
        # return ans if ans > 0 else 0

        t1_cost, t2_cost = float("inf"), float("inf")
        t1_profit, t2_profit = 0, 0

        for price in prices:
            # the maximum profit if only one transaction is allowed
            t1_cost = min(t1_cost, price)
            t1_profit = max(t1_profit, price - t1_cost)
            # reinvest the gained profit in the second transaction
            t2_cost = min(t2_cost, price - t1_profit)
            t2_profit = max(t2_profit, price - t2_cost)

        return t2_profit