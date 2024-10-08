class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # Memoization
        # min_cost = float('inf')
        # memo = {}

        # def helper(rem):
          
            
        #     if rem < 0:
        #         return -1
        #     if rem == 0:
        #         return 0
        #     if rem in memo:
        #         return memo[rem]
        #     # At Each Subproblem, we want to Initialize a big Number as Min_cost   
        #     min_cost = float('inf')
        #     for coin in coins:
        #         res = helper(rem-coin)
        #         if res!=-1:
        #             min_cost = min(min_cost,res+1)
        #     memo[rem] = min_cost if min_cost != float('inf') else -1
        #     return memo[rem]
        # return helper(amount)

        # Tabulation
        MAX = amount+1
        memo = [MAX] * (amount+1)
        memo[0] = 0

        for sub_amount in range(1,amount+1):
            for coin in coins:
                if sub_amount-coin >= 0:
                    memo[sub_amount] = min(memo[sub_amount], memo[sub_amount-coin]+1)
        
        return memo[amount] if memo[amount] < MAX else -1