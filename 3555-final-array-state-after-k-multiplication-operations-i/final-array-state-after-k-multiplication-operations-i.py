import heapq
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        pq = [(val,i) for i, val in enumerate(nums)]
        heapq.heapify(pq)

        while k:
            min_val, idx = heapq.heappop(pq)
            min_val = min_val * multiplier
            heapq.heappush(pq,(min_val, idx))
            k-=1
        
        while pq:
            val, idx = heapq.heappop(pq)
            nums[idx] = val
        
        return nums