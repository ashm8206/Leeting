class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:

        nums.sort()
        n = len(nums)

        ans = 0
        for i in range(0, n-1, 2):
            ans += min(nums[i], nums[i+1])
        
        return ans 
