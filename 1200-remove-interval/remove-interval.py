class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
    
        result = []
        remove_start, remove_end = toBeRemoved
        
        for start, end in intervals:
            # Case 1: No overlap - interval is completely before/after toBeRemoved
            if end <= remove_start or start >= remove_end:
                result.append([start, end])
                continue
                
            # Case 2: If there's a part before toBeRemoved
            if start < remove_start:
                result.append([start, remove_start])
                
            # Case 3: If there's a part after toBeRemoved
            if end > remove_end:
                result.append([remove_end, end])
        
        return result
        
        