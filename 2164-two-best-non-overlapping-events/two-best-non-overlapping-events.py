import heapq
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        
      
        # maxProfit = 0
        # maxVal = 0 
        # # track the most optimal Value Sofar

        # # even if previous event is Popped out, if it gave the maxVal,
        # # that will remain constant, until a greater maxVal shows up

        # # inwhich case it will be counted towards maxVal + currEvent'sProfit

        # # if the previous pair, non-overlapping was indeed so high !
        # # maxProfit will be unchanged for (newMaxVal+newCurrentEventProfit)

        # pq = []

        # for start, end, profit in events:
        #     # Among all Overlapping options available
        #     # pop all non-overlapping intervals with curr
        #     # and keep track of the MaxVal Non-overlapping interval

        #     while pq and start > pq[0][0]: # start >= end Non-overlap condi
        #         _, val = heappop(pq)
        #         maxVal = max(val, maxVal)
            
        #     # At most 2 Overlapping, 
        #     # we just want to find a Pair or Single MaxVal

        #     maxProfit = max(maxProfit, maxVal+profit)

        #     heappush(pq,(end, profit))

        #     # loop invariant: After each iteration heap will have all overlapping interval with their profits

            
        # return maxProfit

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




   
        
