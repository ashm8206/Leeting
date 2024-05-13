class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        tot = len(nums) * (len(nums) - 1) // 2
        good = 0
        hmap = {}
        
        for i,num in enumerate(nums):
            v = i - num
            good += hmap.get(v, 0)
            hmap[v] = hmap.get(v, 0) + 1
        
        return tot - good