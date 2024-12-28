class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # Pair value[i] , value[j] : max(value[j] - value[i])

        minPrice = float("inf")
        ans = float("-inf")
        for j in range(1,n):
            minPrice = min(minPrice,prices[j-1])
            ans = max(ans, prices[j] - minPrice)
        return ans if ans > 0 else 0
