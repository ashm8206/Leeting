class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # Method I - Memoized

        # if sum(nums)%2:
        #     return False

        # memo = {}

        # def dfs(i, target):
        #     if i >= len(nums):
        #         return target == 0
            
        #     if target < 0:
        #         return False
        #     if (i,target) in memo:
        #         return memo[(i,target)]
            
        #     memo[(i,target)] = dfs(i+1, target) or dfs(i+1, target-nums[i])
            
        #     return memo[(i,target)]
        
        # return dfs(0, sum(nums)//2)



        # Neetcode Hashset

        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        return False

        total_sum = sum(nums)
        if total_sum %2:
            return False
        
        subset_sum = total_sum // 2

        dp = [False]*(subset_sum+1)
        dp[0] = True
        for curr in nums:
            for j in range(subset_sum, curr - 1, -1):
                dp[j] = dp[j] or dp[j-curr]
        return dp[subset_sum]