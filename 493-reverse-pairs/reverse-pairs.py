class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        pre = []
        res = 0
        for i in range(len(nums)):
            if not pre:
                pre.append(nums[i])
            else:
                index = bisect.bisect_right(pre,2*nums[i])
                if index < len(pre):
                    res += len(pre) - index
                bisect.insort(pre,nums[i])
        return res
        # worst case, which is O(n log n). 
        # The algorithm as a whole still has a running time of O(n2) on average because of the series of swaps required for each insertion.
        return counts