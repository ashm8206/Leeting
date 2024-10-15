class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # n = len(nums)
        # nums.sort()
        # return max(nums[0]*nums[1]*nums[n-1],nums[n-3]*nums[n-2]*nums[n-1])
        
        # Numbers can be negative
        #  max(3_largest_nums or 1_largest_number_2smallest_numbers)  


        n = len(nums)

        maxCount = float("-inf")

        leftSumMax = [nums[0]]*(n)
        rightSumMax = [nums[n-1]]*(n)

        leftSumMin = [nums[0]]*(n)
        rightSumMin = [nums[n-1]]*(n)

        for i in range(1,n):
            leftSumMax[i] = max(leftSumMax[i-1],nums[i])
            leftSumMin[i] = min(leftSumMin[i-1], nums[i])

        for j in range(n-2,-1,-1):
            rightSumMax[j] = max(rightSumMax[j+1],nums[j])
            rightSumMin[j] = min(rightSumMin[j+1], nums[j])

        for i in range(1,n-1):
            maxProd = leftSumMax[i - 1]* rightSumMax[i + 1] * nums[i]
            minProd = leftSumMin[i - 1]* rightSumMin[i + 1] * nums[i]
            mixProd = max(leftSumMin[i - 1] * rightSumMax[i + 1] * nums[i],
            leftSumMax[i - 1]*rightSumMin[i + 1]*nums[i])

            # two - minus make 1 +
            maxCount = max([maxProd,minProd,mixProd,maxCount])
        return maxCount