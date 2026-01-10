from collections import defaultdict

class Solution:
    # On PASS
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hmap = defaultdict(int)
        maxFreq = 0
        ans = 0
        for num in nums:
            hmap[num]+=1
            freq = hmap[num]

            if freq > maxFreq:
                maxFreq = freq
                ans = freq
            elif freq == maxFreq:
                ans += freq
        return ans
                



       