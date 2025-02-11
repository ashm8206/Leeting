class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False

        memo = {}

        def dfs(i, target):
            if i >= len(nums):
                return target == 0
            
            if target < 0:
                return False
            if (i,target) in memo:
                return memo[(i,target)]
            
            memo[(i,target)] = dfs(i+1, target) or dfs(i+1, target-nums[i])
            
            return memo[(i,target)]
        
        return dfs(0, sum(nums)//2)