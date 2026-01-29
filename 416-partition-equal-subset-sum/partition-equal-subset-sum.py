class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # Method I - Memoized

        if sum(nums)%2:
            return False

        memo = {}
        n = len(nums)
        target = sum(nums)//2
        
        def dfs(i, curr_sum):
            if i >= n:
                return target == curr_sum
            
            if (i,curr_sum) in memo:
                return memo[(i,curr_sum)]
            
            memo[(i,curr_sum)] = dfs(i+1, curr_sum) or dfs(i+1, curr_sum+nums[i])
            
            return memo[(i,curr_sum)]
        
        return dfs(0, 0)



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