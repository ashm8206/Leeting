class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        L = 0
        n = len(nums)
        maxValue = -10**5

        currSum = 0
        for R in range(n):

            currSum+=nums[R]

            if R-L+1 == k:
                maxValue = max(maxValue, currSum/k)
                currSum -= nums[L]
                L+=1
        return maxValue
