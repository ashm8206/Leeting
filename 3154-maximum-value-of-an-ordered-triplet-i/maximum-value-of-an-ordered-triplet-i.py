class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)

        # maxValue = 0
        # for i in range(n-2):
        #     for j in range(i+1,n-1):
        #             for k in range(j+1,n):
        #                 curr_val = (nums[i]-nums[j])*nums[k]
        #                 # print(curr_val)
        #                 maxValue = max(maxValue,max(curr_val,0))
        # return maxValue

        n = len(nums)

        maxCount = 0

        leftSum = [nums[0]]*(n)
        rightSum = [nums[n-1]]*(n)

        for i in range(1,n):
            leftSum[i] = max(leftSum[i-1],nums[i])

        for j in range(n-2,-1,-1):
            rightSum[j] = max(rightSum[j+1],nums[j])
        

        for i in range(1,n-1):
            maxCount = max(maxCount, (leftSum[i - 1] - nums[i]) * rightSum[i + 1])
            # res = Math.max(res, (maxLeft[i - 1] - nums[i]) * maxRight[i + 1]);

        return maxCount
