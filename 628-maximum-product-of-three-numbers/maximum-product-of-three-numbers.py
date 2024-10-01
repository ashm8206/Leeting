class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        return max(nums[0]*nums[1]*nums[n-1],nums[n-3]*nums[n-2]*nums[n-1])
        
        # Numbers can be negative
        #  max(3_largest_nums or 1_largest_number_2smallest_numbers)  