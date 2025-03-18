class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        # Aggresssive COW

        start.sort()
        # sort when K is a func of distance on number line

        def isPossible(mid):
            x = -inf
            for s in start:
                x+=mid
                if x > s+d:
                    return False
                x = max(x,s)
            return True

        l = 0
        r = start[-1] + d - start[0]

        while l < r:
            mid = (l+r+1) // 2
            if isPossible(mid):
                l = mid
            else:
                r = mid - 1
        return l


