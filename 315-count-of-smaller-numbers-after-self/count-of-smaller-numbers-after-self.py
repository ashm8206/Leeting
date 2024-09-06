class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        counts = []
        done = []
      
        for num in nums[::-1]:
            idx=bisect.bisect_left(done, num)
            counts.append(idx)
    
            bisect.insort(done, num)

        # worst case, which is O(n log n). 
        # The algorithm as a whole still has a running time of O(n2) on average because of the series of swaps required for each insertion.
        return counts[::-1]