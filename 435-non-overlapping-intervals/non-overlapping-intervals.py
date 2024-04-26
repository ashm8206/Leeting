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
                # since it will not cause anymore overlaps
            else:
                # not overlaping
                e1 = e2
        
        return ans

        # Remove largest Overlap, increasingly
        # 1 2, 1, 3, 2,3,  3, 4
    
  
