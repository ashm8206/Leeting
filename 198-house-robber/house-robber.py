class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return nums[0]
            
        dp = [0]* n
        dp[0] = nums[0]
        dp[1] = max(nums[1] + 0, nums[0])
        
        for i in range(2, n):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])
        
        return dp[-1]

        
        # choice 1 either rob from house i and add maxRobScore i-2 house
        # choice 2 rob from previous house to i 
        # think about initializing the scores
        
        # at ith Dp store the most optimal score. 
        return dp[n]
        


        # nums(k) # make money kth house
        # dp[k] = max(dp[i-2]+nums[k], dp[i-1])
            




        