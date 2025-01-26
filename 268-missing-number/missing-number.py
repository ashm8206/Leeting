class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        mask = n
        x = 0
        for i in range(n):
            mask^=i
            x^=nums[i]
            
        return x ^ mask
        