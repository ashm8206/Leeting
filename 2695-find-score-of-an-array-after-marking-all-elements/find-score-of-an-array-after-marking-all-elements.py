import heapq
class Solution:
    def findScore(self, nums: List[int]) -> int:
        #  while minHeap:
            #  while minheap and minHeapTop[0][1] in markedMap:
                # Keep popping 
            #  Var Score+=  add minHeap(top) Pop (not marked found:)
            #  markedMap :  add  to it
        score = 0
        nums = [(val, i) for i, val in enumerate(nums)]
        markedSet = set()
        n = len(nums)

        heapq.heapify(nums)
        while nums:

            val, idx = heapq.heappop(nums)
            if idx in markedSet:
                continue

            score += val
            markedSet.add(idx)

            if idx < n-1:
                markedSet.add(idx+1)
            if idx-1>=0:
                markedSet.add(idx-1)

        return score