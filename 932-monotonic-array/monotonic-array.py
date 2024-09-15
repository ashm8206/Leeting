class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        n = len(nums)
    
        increasing =  True if nums[0] < nums[n-1] else False

        for i in range(1,n):
            if increasing and nums[i-1] > nums[i]:
                return False
            if not increasing and nums[i-1] < nums[i]:
                return False
        return True