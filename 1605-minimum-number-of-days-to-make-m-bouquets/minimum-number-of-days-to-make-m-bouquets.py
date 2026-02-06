class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        def feasible(maxWaitDay):
            streak = 0
            cnt_bq = 0
            for day in bloomDay:
                if day <= maxWaitDay:
                    streak+=1
                else:
                    streak = 0
                
                if streak == k:
                    cnt_bq+=1
                    streak = 0
            return cnt_bq >= m


        l = 1 
        r = max(bloomDay)

        while l < r:
            mid = (l+r)//2
            if feasible(mid):
                r = mid
            else:
                l = mid + 1
        
        if feasible(l):
            return l 
        return -1