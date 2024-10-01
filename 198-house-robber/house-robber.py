class Solution:
    def rob(self, nums: List[int]) -> int:
        

        n = len(nums)
        dp = [0]*(n+1)
        
        dp[0] = 0
        dp[1] = nums[0]
    

        # [1,2,3,1] --> 
        # take 1 or take 2 with 0 
        # take 2 or take 3+1
        for i in range(2,n+1):
            dp[i] = max(nums[i-1]+dp[i-2], dp[i-1])
        
        # choice 1 either rob from house i and add maxRobScore i-2 house
        # choice 2 rob from previous house to i 
        # think about initializing the scores
        
        # at ith Dp store the most optimal score. 
        return dp[n]
        


        # nums(k) # make money kth house
        # dp[k] = max(dp[i-2]+nums[k], dp[i-1])
            




        