from collections import defaultdict

class HitCounter:
    """
    A counter that tracks the number of hits within a 5-minute window.
    - hit(): O(1) time complexity
    - getHits(): O(log n) time complexity, where n is the number of unique timestamps
    - Space complexity: O(n) where n is the number of unique timestamps
    """

    def __init__(self):
        self.timestamps = []
        self.l = 0

    def hit(self, timestamp: int) -> None:
        self.timestamps.append(timestamp)
        self.l += 1
        
    def getHits(self, timestamp: int) -> int:

        # You have to find number of hits in range:
        # [timestamp-300 + 1, timestamp]

        left = 0
        right = self.l-1
        target = timestamp - 300
        # right most binary search
        while left <= right:
            m = (left + right) // 2
            if self.timestamps[m] <= target:
                left = m + 1
            else:
                right = m - 1

        return self.l - left        
        
# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)