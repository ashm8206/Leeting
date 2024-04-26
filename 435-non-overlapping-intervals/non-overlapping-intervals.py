class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        ans = 0
        e1 = -inf
        
        for s2, e2 in intervals:
            if s2 < e1:
                # Overlap
                ans+=1
                e1 = min(e1,e2)
                # Update to the smaller value
                # since it will not cause anymore overlaps
                # Remove the larger end value
            else:
                # not overlaping
                e1 = e2
        
        return ans

    
  
