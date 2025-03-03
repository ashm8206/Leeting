from collections import defaultdict

class HitCounter:
    """
    A counter that tracks the number of hits within a 5-minute window.
    - hit(): O(1) time complexity
    - getHits(): O(log n) time complexity, where n is the number of unique timestamps
    - Space complexity: O(n) where n is the number of unique timestamps
    """
    def __init__(self):
        # List of [timestamp, cumulative_count] pairs
        self.hits = [[0, 0]]
        
    def hit(self, timestamp: int) -> None:
        # If hit at same timestamp, update the count
        if self.hits[-1][0] == timestamp:
            self.hits[-1][1] += 1
        else:
            # Add new timestamp with count incremented by 1
            self.hits.append([timestamp, self.hits[-1][1] + 1])
            
    def getHits(self, timestamp: int) -> int:
        # Find the position for current timestamp
        current_idx = self.binary_search(timestamp)
        # Find the position for timestamp - 300 (5 minutes ago)
        past_idx = self.binary_search(timestamp - 300)
        
        # Return the difference in cumulative counts
        return self.hits[current_idx][1] - self.hits[past_idx][1]
    
    def binary_search(self, target: int) -> int:
        left, right = 0, len(self.hits)
        
        # Find the insertion point
        while left < right:
            mid = (left + right) // 2
            if self.hits[mid][0] <= target:
                left = mid + 1
            else:
                right = mid
                
        # Adjust to get the timestamp that's <= target
        idx = left - 1 if left > 0 else 0
        
        # If we've gone past the target, go back one step
        if idx < len(self.hits) and self.hits[idx][0] > target:
            idx = max(0, idx - 1)
            
        return idx
        


        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)