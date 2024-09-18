class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        min_cost = float('inf')
        memo = {}
        def helper(rem):
          
            
            if rem < 0:
                return -1
            if rem == 0:
                return 0
            if rem in memo:
                return memo[rem]
            # at each choice, we want to  minimize    
            min_cost = float('inf')
            for coin in coins:
                res = helper(rem-coin)
                if res!=-1:
                    min_cost = min(min_cost,res+1)
            memo[rem] = min_cost if min_cost != float('inf') else -1
            return memo[rem]
        return helper(amount)