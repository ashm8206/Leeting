class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        hmap = Counter(nums)

        res = []
        for num in nums:
            if (num-1) in hmap  or (num+1) in hmap or hmap[num] > 1:
                continue
            else:
                res.append(num)
        return res