class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        
        n = len(nums)

        dp = [-1 for i in range(n)]

        dp[0] = 0  # you can jump from 0 to 0 in 0 jumps

        for i in range(1, n):
            for j in range(0, i):
                if abs(nums[i]-nums[j]) <= target and dp[j]!=-1:
                    dp[i] = max(dp[i], dp[j]+1)
                    # dp[j]!=-1: means we should've reached here before
        return dp[n-1] 