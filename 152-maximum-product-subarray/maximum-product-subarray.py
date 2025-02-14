class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProduct = -10**9
        # maxSoFar = -10**9
        # minSoFar = 10**9

        n = len(nums)


        prefix, suffix, max_so_far = 0, 0, float('-inf')
        for i in range(n):
            prefix = (prefix or 1) * nums[i]
            suffix = (suffix or 1) * nums[n-1-i] # same as ~i
            max_so_far = max(max_so_far, prefix, suffix)
        return max_so_far
        
        
        maxSoFar = nums[0]
        minSoFar = nums[0]

        maxProduct = nums[0]

        for i in range(1,n):
            # -11, 11 ,  22
            # nums[i] = -11
            # maxSoFar = -1
            # minSoFar = -2
            currProd = max(nums[i], max(maxSoFar*nums[i],minSoFar*nums[i]))
            maxProduct = max(currProd,maxProduct)

            currMax= maxSoFar*nums[i] # assumed currMax
            currMin = minSoFar*nums[i]

            # by multiplying with curr nums[i]. both maxSofar and minSofar can change.
            # take the following comparison between 3 values to get NExt maxSoFar and minSoFar

            maxSoFar = max(nums[i], max(currMax,currMin))
            minSoFar = min(nums[i], min(currMax,currMin))
        return maxProduct

        