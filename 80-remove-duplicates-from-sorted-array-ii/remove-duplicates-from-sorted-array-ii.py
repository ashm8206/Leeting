class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # https://www.youtube.com/watch?v=ycAq8iqh0TI
        # count, r, l,= 1, 0, 0
        # while r < len(nums):
        #     count = 1
        #     while r+1 < len(nums) and nums[r]==nums[r+1]:
        #         r+=1
        #         count+=1
            
        #     for i in range(min(2,count)):
        #         nums[l]=nums[r] # first occurrence
        #         l+=1
        #     r+=1
        # return l

        # Method II

        nextIndex = 0
        n = len(nums)

        for reader in range(n):
            # uptil i <= 1 the idx
            if nextIndex <=1 or nums[reader]!=nums[nextIndex-2]:
                nums[nextIndex]= nums[reader]
                nextIndex+=1
        return nextIndex

        