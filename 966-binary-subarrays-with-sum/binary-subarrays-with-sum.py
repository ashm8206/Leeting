class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        count = 0
        sums = 0
        hmap = {0:1}

        for i in range(len(nums)):
            sums += nums[i]
            if (sums - goal) in hmap:
                count += hmap.get(sums - goal)
            hmap[sums] = hmap.get(sums,0) + 1
        return count
        