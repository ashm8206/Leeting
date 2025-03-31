class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        
        def feasible(mid):
            count = 0
            for i in range(len(stations)-1):
                count += (stations[i+1]-stations[i])// mid 
            return count <=k

        l = 0
        r = max(stations)
        
        while r - l > 1e-6:
            mid = (l+r)/2.0
            if feasible(mid):
                r = mid 
            else:
                l = mid 
        return l
