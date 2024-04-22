class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        
        n = len(nums)
        leftSum = [nums[0]]*(n)
        rightSum = [nums[n-1]]*(n)

        for i in range(1,n):
            leftSum[i] = min(leftSum[i-1],nums[i])

        for j in range(n-2,-1,-1):
            rightSum[j] = min(rightSum[j+1],nums[j])
        
        minSum = 10**5

        # print(leftSum,rightSum)

        for i in range(1, n-1):
            #for every peak
            # Peak is not strictly next, but every previous element
            if leftSum[i-1] < nums[i] > rightSum[i+1]:
                minSum = min(minSum, leftSum[i-1]+nums[i]+rightSum[i+1])
        
        return minSum if minSum != 10**5 else -1




