from collections import defaultdict

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hmap = defaultdict(int)
        FreqCount = defaultdict(int)

        maxFreq = 0
        for num in nums:
            hmap[num]+=1
            maxFreq = max(maxFreq,hmap[num])

        ans = 0
        for k, v in hmap.items():
            if v == maxFreq:
                ans+=maxFreq
        return ans
        