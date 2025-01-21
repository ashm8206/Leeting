class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:

        ways = 0
        odd_after, even_after = sum(nums[1::2]), sum(nums[0::2])
        odd_before, even_before = 0, 0
        
        for i, num in enumerate(nums):
            if i % 2 == 0:
                even_after -= num

                if even_after + odd_before == odd_after + even_before:
                    ways += 1

                even_before += num
            else:
                odd_after -= num

                if odd_after + even_before == odd_before + even_after:
                    ways += 1
                odd_before += num
                    
        return ways