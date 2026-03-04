class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        count = target[0]
        n = len(target)
        for i in range(1, n):
            count += max(target[i] - target[i-1], 0)
        # When target[i] > target[i-1], you need new strokes to cover the increase. 
        # When it drops, existing strokes from the left just stop — no new ops req
        return count