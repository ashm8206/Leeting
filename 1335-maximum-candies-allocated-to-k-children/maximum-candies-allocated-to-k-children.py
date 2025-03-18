class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        

        def feasible(max_candies):
            piles = 0
            for cand in candies:
                piles += cand // max_candies
            return piles >= k


        l = 0
        r = max(candies)

        while l < r:
            mid = (l + r + 1) // 2
            if feasible(mid):
                l = mid
            else:
                r = mid-1
        return l

        # When using while (left < right) pattern in bsearch, if you do left = mid, you can get an infinite loop since integer division truncates down (floor), hence, we need to round up (ceil) so adding 1 will allow this and adding 1 will help