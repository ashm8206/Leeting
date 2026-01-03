from collections import Counter
import heapq
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        windowSize = n - k + 1

        res = [0] * windowSize
        for i in range(windowSize):
            res[i] = self.topKSum(nums[i:i+k], x)
        return res


    def topKSum(self, nums, x):
        freqCount = Counter(nums)
        minheap = []

        for k, v in freqCount.items():
            heapq.heappush(minheap,(v, k))
            if len(minheap) > x:
                heapq.heappop(minheap)

        topKSum = 0
        while minheap:
            value, num = heapq.heappop(minheap)
            topKSum+= (value * num)
        return topKSum



