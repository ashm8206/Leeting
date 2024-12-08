import heapq
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        
        events.sort(key = lambda x: x[0])
        maxProfit = 0
        maxVal = 0 
        # track the most optimal Value Sofar

        # even if previous event is Popped out, if it gave the maxVal,
        # that will remain constant, until a greater maxVal shows up

        # inwhich case it will be counted towards maxVal + currEvent'sProfit

        # if the previous pair, non-overlapping was indeed so high !
        # maxProfit will be unchanged for (newMaxVal+newCurrentEventProfit)

        pq = []

        for start, end, profit in events:
            # Among all Overlapping options available
            # pop all non-overlapping intervals with curr
            # and extend curr with Most profitable Non-overlapping interval

            while pq and start > pq[0][0]: # start >= end Non-overlap condi
                _, val = heappop(pq)
                maxVal = max(val, maxVal)
            
            # At most 2 Overlapping, 
            # we just want to find a Pair or Single MaxVal

            maxProfit = max(maxProfit, maxVal+profit)

            heappush(pq,(end, profit))

            # loop invariant: After each iteration heap will have all overlapping interval with their profits

            
        return maxProfit