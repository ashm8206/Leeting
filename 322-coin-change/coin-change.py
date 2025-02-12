class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # # # Memoization

        memo = {}

        def dfs(i, amount):
            if amount == 0:
                return 0
            
            if i >= len(coins):
                return float("inf")
            
            if (i, amount) in memo:
                return memo[(i, amount)]
            
            res = dfs(i+1,amount)
            if amount - coins[i] >= 0:
                res = min(res, 1 + dfs(i, amount-coins[i]))
            memo[(i,amount)] = res
            return memo[(i,amount)]

        ans = dfs(0,amount)
        return -1 if ans== float("inf") else ans

       
        # memo = {}
        
        # def dfs(i, amount):
        #     if amount == 0:
        #         return 0
            
        #     if i >= len(coins):
        #         return float('inf')
            
        #     # Check if state already computed
        #     if (i, amount) in memo:
        #         return memo[(i, amount)]
            
        #     # Skip current coin
        #     min_coins = dfs(i + 1, amount)
            
        #     # Include current coin if possible
        #     if amount - coins[i] >= 0 :
        #         min_coins = min(min_coins, 1 + dfs(i, amount - coins[i]))
                
        #     memo[(i, amount)] = min_coins
        #     return min_coins
        
        # result = dfs(0, amount)
        # return result if result != float('inf') else -1
            
            
        


        min_cost = float('inf')
        memo = {}

        def helper(rem):
          
            
            # if rem < 0:
            #     return -1
            if rem == 0:
                return 0
            if rem in memo:
                return memo[rem]
            # At Each Subproblem, 
            # we want to Initialize a big Number as Min_cost

            min_cost = float('inf')
            for coin in coins:
                if rem-coin >= 0:
                    res = helper(rem-coin)
                    if res!=-1:
                        min_cost = min(min_cost,res+1)
            memo[rem] = min_cost if min_cost != float('inf') else -1
            return memo[rem]
        return helper(amount)

        # # Tabulation
        # MAX = amount+1
        # memo = [MAX] * (amount+1)
        # memo[0] = 0

        # for sub_amount in range(1,amount+1):
        #     for coin in coins:
        #         if sub_amount-coin >= 0:
        #             memo[sub_amount] = min(memo[sub_amount], memo[sub_amount-coin]+1)
        
        # return memo[amount] if memo[amount] < MAX else -1