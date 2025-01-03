class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # https://www.youtube.com/watch?v=I7j0F7AHpb8

        dp = {}
        def dfs(i, buying):
            if i>=len(prices):
                return 0 # 0 profit

            if (i, buying) in dp:
                return dp[(i, buying)]
            
            if buying:
                buy = dfs(i+1, not buying) - prices[i] # cant keep buying 
                # sell and cooldown
                cooldown = dfs(i+1, buying)
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i+2, not buying) + prices[i]
                # i+2 skip 1 day
                cooldown = dfs(i+1, buying)
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]
        return dfs(0, True) # only buy at the begining
            
            
