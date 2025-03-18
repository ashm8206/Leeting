class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        def feasible(max_days):
            cnt_boq = 0
            flower_streak = 0 # k streak
            for day in bloomDay:
                if day <= max_days:
                    flower_streak+=1
                else:
                    flower_streak = 0

                if flower_streak == k:
                    cnt_boq +=1
                    flower_streak = 0
            return cnt_boq >= m
                
        l = 1
        r = max(bloomDay)
        
        while l < r:
            mid = (l + r) // 2
            if feasible(mid):
                r = mid
            else:
                l = mid + 1
        
        if feasible(l):
            return l
        return -1
