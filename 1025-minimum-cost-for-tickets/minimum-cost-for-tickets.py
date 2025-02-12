class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
    
        n = len(days)
        dp = {}
        
        def dfs(i):
            if i == n:
                return 0

            if i in dp:
                return dp[i]
            
            dp[i] = float("inf")
            j = i
            for duration, cost in zip([1,7,30],costs):
                while j < n and days[j] < days[i] + duration:
                    j+=1
                
                dp[i]= min(dp[i], cost + dfs(j))
                # print(i, days[i], cost + dfs(j), j ,duration)
            # print("---")
            return dp[i]
        
        return dfs(0)