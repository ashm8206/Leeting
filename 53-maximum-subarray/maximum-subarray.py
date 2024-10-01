class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        

        n = len(nums)
        a = nums[:]

        dp = [0 for i in range(n)]
        dp[0] = a[0]
        maxSofar = a[0]

        for i in range(1,n):
        
            dp[i] = max(dp[i-1]+a[i], a[i])
                # Every time, we check, 
                # dp[i] = what is max ? a[i] # by itself or  continuation
    
           
            # Every Time
            # TestCase  [5,-1,-1,-1,-1,-1] MaxSum 5 !
            maxSofar = max(maxSofar, dp[i])
        return maxSofar