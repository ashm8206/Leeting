class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        

        def feasible(max_candies):
            piles = 0
            for cand in candies:
                piles += math.ceil(cand//max_candies)
            return piles >= k


        l = 0
        r = max(candies)

        while l < r:
            mid = (l + r + 1) // 2 
            # Righmost BS , so add 1, there start from l = 0
            if feasible(mid):
                l = mid
            else:
                r = mid-1
        return l

        # When using while (left < right) pattern in bsearch, if you do left = mid, you can get an infinite loop since integer division truncates down (floor), hence, we need to round up (ceil) so adding 1 will allow this and adding 1 will help



#  Meguru method
# ok = 0  # always possible to give 0 candies to k children
# ng = sum(candies) // k + 1  # impossible to give this number of candies to k children
# while abs(ok - ng) > 1:  # depending on the problem it can be ok > ng
#     mid = (ok + ng) // 2
#     if check(mid):  # check whether mid is feasible
#         ok = mid
#     else:
#         ng = mid
# return ok