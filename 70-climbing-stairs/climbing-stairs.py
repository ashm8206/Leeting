class Solution:
    def climbStairs(self, n: int) -> int:
        memo = dict()
        memo[0] = 0 # add this for potential key error
        memo[1] = 1
        memo[2] = 2


        for i in range(3,n+1):
            memo[i] = memo[i-1] + memo[i-2]
        
        return memo[n]






