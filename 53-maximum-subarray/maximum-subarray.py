class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # Method I
        # n = len(nums)
        # a = nums[:]

        # dp = [0 for i in range(n)]
        # dp[0] = a[0] 
        # # you have to give valid subarray , empty subarray wwith zero not allowed
        # maxSofar = a[0]

        # for i in range(1,n):
        
        #     dp[i] = max(dp[i-1]+a[i], a[i])
        #         # Every time, we check, 
        #         # dp[i] = what is max ? a[i] # by itself or  continuation
        #     # Every Time
        #     # TestCase  [5,-1,-1,-1,-1,-1] MaxSum 5 !
        #     maxSofar = max(maxSofar, dp[i])
        # return maxSofar

        # Method II 
        # https://www.youtube.com/watch?v=HCL4_bOd3-4

        maxSum = nums[0]
        currSum = 0
        n = len(nums)

        for i in range(n):
            currSum += nums[i]
            maxSum = max(maxSum, currSum)

            if currSum < 0:
                currSum = 0
        return maxSum