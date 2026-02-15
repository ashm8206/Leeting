from collections import defaultdict
import bisect
class HitCounter:
    """
    A counter that tracks the number of hits within a 5-minute window.
    - hit(): O(1) time complexity
    - getHits(): O(log n) time complexity, where n is the number of unique timestamps
    - Space complexity: O(n) where n is the number of unique timestamps
    """

    def __init__(self):
        self.timestamps = deque()
        

    def hit(self, timestamp: int) -> None:
        self.timestamps.append(timestamp)
        
        
    def getHits(self, timestamp: int) -> int:
        if not self.timestamps:
            return 0

        # target = timestamp - 299
        # left = bisect.bisect_left(self.timestamps, target)

        left, right = 0, len(self.timestamps)
        target = timestamp - 300 + 1
    
        while left < right:
            mid = (left + right) // 2

            if self.timestamps[mid] >= target:
                right = mid
            else:
                left = mid + 1

            
        return len(self.timestamps) - left

        #Method II
        while self.timestamps and  self.timestamps[0] <= timestamp - 300:
            self.timestamps.popleft()
        return len(self.timestamps)
        
# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)