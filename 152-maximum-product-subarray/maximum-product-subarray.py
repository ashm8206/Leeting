class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProduct = -10**9
        maxSoFar = -10**9
        minSoFar = 10**9

        n = len(nums)
        dp =[0]*n
        dp_min = [0] * n

        dp[0] = nums[0]
        dp_min[0] = nums[0]

        for i in range(n):
            if i > 0:
                dp[i] = max([dp[i-1]*nums[i], dp_min[i-1]*nums[i], nums[i]])
                dp_min[i] = min([dp[i-1]*nums[i],dp_min[i-1]*nums[i], nums[i]])
            else:
                dp[i] = nums[i]
                dp_min[i] = nums[i]

            maxProduct = max([maxProduct, dp[i]])
        return maxProduct
        
       
        # for i in range(n):
        #     tempProd = max(nums[i], max(maxSoFar*nums[i],minSoFar*nums[i]))
        #     maxProduct = max(tempProd,maxProduct)
        #     maxSoFar = max(nums[i], max(maxSoFar*nums[i],minSoFar*nums[i]))
        #     minSoFar = min(nums[i], min(maxSoFar*nums[i],minSoFar*nums[i]))
        # return maxProduct

        