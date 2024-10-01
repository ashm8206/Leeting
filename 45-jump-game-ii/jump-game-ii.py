class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [float("inf") for i in range(n)]

        dp[0] = 0  # you can jump from 0 to 0 in 0 jumps

        for i in range(n):
            for j in range(0, nums[i]+1):
                if i+j < n:
                    dp[i+j] = min(dp[i+j], dp[i]+1)
                 
        return dp[n-1] 