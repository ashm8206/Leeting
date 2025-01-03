class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
            # FSM: k bought states and k sold states
    # transaction = buy then sell. so we will increment after buying because we are now in a new transaction regardless of if we sell. we're already "commited" to the transaction
    #   * bought[number_of_transactions] is max(bought[n_of_t], sold[n_of_t-1] - price)
    #   * sold[number_of_transactions] is max(sold[n_of_t], bought[n_of_t] + price)
    #   * sold[i-1] - price --> bought[i] because it's a new transaction

        bought = [-inf] * (k + 1)
        sold = [0] * (k + 1)
        maxProfitVal = 0

        for price in prices:
            for i in range(1, k + 1):
                bought[i] = max(bought[i], sold[i - 1] - price)
                sold[i] = max(sold[i], bought[i] + price)
                maxProfitVal = max(maxProfitVal, sold[i])

        return maxProfitVal