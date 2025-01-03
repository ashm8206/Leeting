class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
            # FSM: k bought states and k sold states
    # transaction = buy then sell. so we will increment after buying because we are now in a new transaction regardless of if we sell. we're already "commited" to the transaction
    #   * bought[number_of_transactions] is max(bought[n_of_t], sold[n_of_t-1] - price)
    #   * sold[number_of_transactions] is max(sold[n_of_t], bought[n_of_t] + price)
    #   * sold[i-1] - price --> bought[i] because it's a new transaction

        if not k:
            return k
        t_cost = [float('inf')] * k
        t_profit = [0] * k

        for price in prices:
            t_cost[0] = min(t_cost[0], price)
            t_profit[0] = max(t_profit[0], price - t_cost[0])
            for i in range(1, k):
                t_cost[i] = min(t_cost[i], price - t_profit[i - 1])
                t_profit[i] = max(t_profit[i], price - t_cost[i])
    
        return t_profit[-1]