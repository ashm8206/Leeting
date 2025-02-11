class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        memo = {}

        def dfs(i, amount):
            if amount == 0:
                return 1
            
            if i >= len(coins):
                return 0

            if (i,amount) in memo:
                return memo[(i,amount)]
            

            res = dfs(i+1, amount)
            if amount - coins[i] >= 0:
                res += dfs(i, amount - coins[i])
    
            memo[(i,amount)] = res
            return memo[(i,amount)] 
        
        return dfs(0, amount)
    


        
        # BackTracking/ memoizatiom TimeOt
        # numWays = 0
        # n = len(coins)

        # memo = {}
        # @cache
        # def helper(rem, idx):
        #     # nonlocal numWays
        #     if rem==0:
        #         # numWays+=1
        #         return 1
        #     if rem < 0:
        #         return 0
        #     if (rem,idx) in memo:
        #         return memo[(rem,idx)]

        #     combs: int = 0
        #     for i in range(idx, n):
                
        #         combs+=helper(rem-coins[i],i) # i can be taken repeated times. Hence no i+1
        #     memo[(rem,idx)] = combs
        #     return memo[(rem,idx)]
        # return helper(amount,0)

        # return numWays

        n = len(coins)
        M = [[0 for i in range(amount+1)] for x in range(n+1)]
        for i in range(n+1):
            M[i][0] = 1
    
        for i in range(1, n+1):
            for j in range(1, amount+1):
                if coins[i-1] > j:
                    M[i][j] = M[i-1][j]
                else:
                    M[i][j] = M[i-1][j] + M[i][j-coins[i-1]]
        return M[n][amount]

        # dp = [0] * (amount + 1)
        # dp[0] = 1

        
        # for coin in coins:
        #     for sub_amount in range(coin, amount+1):
        #         if sub_amount - coin >= 0:
        #             dp[sub_amount] += dp[sub_amount - coin]
        # return dp[amount]