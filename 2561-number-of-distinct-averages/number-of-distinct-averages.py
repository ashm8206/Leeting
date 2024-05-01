class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        res = set()

        nums.sort()
        i = 0
        j = len(nums)-1
        while i < j:
            res.add((nums[i]+nums[j])/2)
            i+=1
            j-=1
        return len(res)