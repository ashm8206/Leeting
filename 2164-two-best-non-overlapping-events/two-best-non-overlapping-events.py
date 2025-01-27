import heapq
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:

        maxProfit = 0
        maxVal = 0

        events.sort(key = lambda x: x[0])

        n = len(events)

        pq = []
        for i in range(n):
            start, end, curr_profit = events[i]

            while pq and  pq[0][0] < start:
                _, val = heapq.heappop(pq)
                maxVal = max(maxVal,val)
            
            maxProfit = max(maxProfit, curr_profit + maxVal)

            heapq.heappush(pq, (end, curr_profit))

            # while pq and pq[0][0] < start: 
            #     # noOverlap
            #     _, val = heapq.heappop(pq)
            #     maxVal = max(val, maxVal)
            
            # maxSum = max(maxSum, curr_profit + maxVal)
            # # keep the overlapping in a queue
            # heapq.heappush(pq, (end, curr_profit))

        return maxProfit

        '''
        By processing events in order of start time and maintaining a min heap of end times, we can efficiently find non-overlapping events.
For each event, we:

    1. Remove all completed events (events that end before current event starts) from heap
2. Keep track of maximum profit seen from any completed event (maxVal)
3. Try combining current event's profit with best completed event's profit
4. Add current event to heap for future consideration

        '''





        # LIS - Like Pattern
        # Keep all overlapping intervals in a Heap
        # for each new curr interval, 
            # check if non-overlapping with all overlapping options in heap
            # if Non-overlapping, get the maxVal they contribute
        
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




   
        
