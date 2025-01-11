class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        ans = []
        nums = mountain
        n = len(nums)
        for i in range(1,n-1):
            if nums[i-1] < nums[i] > nums[i+1]:
                ans.append(i)
        return ans
