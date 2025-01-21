class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        even_remain, odd_remain = sum(nums[::2]), sum(nums[1::2])
        even_curr, odd_curr, result = 0, 0, 0
        for i, num in enumerate(nums):
            if i % 2 == 0:
                even_remain -= num
                result += (even_curr + odd_remain == odd_curr + even_remain)
                even_curr += num
            else:
                odd_remain -= num
                result += (even_curr + odd_remain == odd_curr + even_remain)
                odd_curr += num
        return result