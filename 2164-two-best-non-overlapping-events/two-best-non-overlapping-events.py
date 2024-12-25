import heapq
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        
        events.sort()
        
        maxProfit = 0
        maxVal = 0 

        pq = []

        for start, end, profit in events:

            while pq and start > pq[0][0]: # start >= end Non-overlap condi
                _, val = heappop(pq)
                maxVal = max(val, maxVal)
            
            # At most 2 Overlapping, 
            # we just want to find a Pair or Single MaxVal

            heappush(pq,(end, profit)) # dont add extended

        #     # loop invariant: After each iteration heap will have all overlapping interval with their profits
            maxProfit = max(maxProfit, maxVal+profit)
        return maxProfit



        # line - Sweep
        times = []
        for e in events:
            # 1 denotes start time.
            times.append([e[0], 1, e[2]])
            # 0 denotes end time.
            times.append([e[1] + 1, -1, e[2]])

        times.sort()

        ans = 0
        max_value = 0

        for t, cmd, profit in times:
            if cmd > 0:
                ans = max(ans, profit+ max_value)
            else:
                max_value = max(max_value, profit)
        return ans




   
        
