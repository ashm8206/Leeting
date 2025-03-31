class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        
        def can_reach_on_time(speed):
            total_hours = 0.0
            n = len(dist)
            for i in range(n-1):
                total_hours+= math.ceil(dist[i]/speed)
            total_hours+= dist[n-1]/speed
            return total_hours<=hour


        left, right = 1, 10**7
        while left < right:
            mid = (left + right) // 2
            if can_reach_on_time(mid):
                right = mid
            else:
                left = mid + 1
        
        if can_reach_on_time(left):
            return left
        else:
            return -1