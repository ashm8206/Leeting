class Solution:
    def singleNumber(self, nums: List[int]) -> int:
       
        ones = 0
        twos = 0

        for num in nums:
            ones ^= (num & ~twos) # (ones ^ i) & (~twos)
            
            twos ^= (num & ~ones) # (twos ^ i) & (~ones)

        return ones

        # https://leetcode.com/problems/single-number-ii/solutions/3714928/bit-manipulation-c-java-python-beginner-friendly
