class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:

        total_sum = sum(nums)
        num_splits = 0
        curr_sum = 0
        n = len(nums)

        for i in range(n-1):
            curr_sum+= nums[i]
            right_sum = total_sum - curr_sum
            if curr_sum >= right_sum:
                num_splits+=1
        return num_splits
