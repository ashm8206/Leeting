import heapq
class Solution:
    def findScore(self, nums: List[int]) -> int:
        #  while minHeap:
            #  while minheap and minHeapTop[0][1] in markedMap:
                # Keep popping 
            #  Var Score+=  add minHeap(top) Pop (not marked found:)
            #  markedMap :  add  to it
        score = 0
        pq = [(val, i) for i, val in enumerate(nums)]
        markedSet = set()
        n = len(pq)

        heapq.heapify(pq)
        while pq:

            if len(markedSet)==n:
                break

            while pq and pq[0][1] in markedSet:
                # print("Before",pq)
                heapq.heappop(pq)
                # print("After" , pq)
            
            val, idx = heapq.heappop(pq)
            score += val
            markedSet.add(idx)

            if idx+1 < n:
                markedSet.add(idx+1)
            if idx-1>=0:
                markedSet.add(idx-1)

            # print(score, markedSet)
            # print("--------")
        return score