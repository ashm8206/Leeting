class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # leftmost BS
        l = 0
        r = len(nums)

        while l < r:
            mid = (l+r)//2

            if nums[mid]>=target:
                r = mid
            else:
                l = mid + 1
        return l