class Solution:
    def jump(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [float("inf") for i in range(n)]
        dp[0] = 0
        for i in range(n):
            for j in range(1, nums[i]+1):
                if i+j < n:
                    dp[i+j] = min(dp[i]+1, dp[i+j])

        return dp[n-1]
        # 0 <= j <= nums[i] and
        # i + j < n
