class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def feasible(max_value):
            days_used = 1
            curr_wt = 0
            for wt in weights:
                if curr_wt + wt <= max_value:
                    curr_wt+= wt
                else:
                    days_used+=1 # use another day
                    curr_wt = wt
            return days_used <= days

        l = max(weights) # atleast as large as this
        r = sum(weights)

        while l < r:
            mid = (l+r)// 2
            if feasible(mid):
                r = mid
            else:
                l = mid + 1
        return l