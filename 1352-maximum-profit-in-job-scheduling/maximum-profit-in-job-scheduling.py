from heapq import heappush, heappop
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        n = len(startTime)
        events = []
        for i in range(n):
            # 1 for start event
            # 0 for end event
            # We want end events to occur before start event for same time
            events.append((startTime[i], 1, i))
            events.append((endTime[i], 0, i))
            
        events.sort()
        
        maxProfit = [0]*n
        previousMax = 0
        
        for time, eventType, index in events:
			# If it is a start event, calculate its maximum profit, using previous maximum profit
            if eventType == 1:
                maxProfit[index] = previousMax + profit[index]
			# If it is an end, update previous maximum profit
            else:
                previousMax = max(maxProfit[index], previousMax)
            
        return previousMax

        


        # LIS - Like Pattern
        # Keep all overlapping intervals in a Heap
        # for each new curr interval, 
            # check if non-overlapping with all overlapping options in heap
            # if Non-overlapping, get the maxVal they contribute
        
        # extend this current_interval and add it to the Heap
        # keep track of maxProfit in a sperate variable

        # jobs = []
        # for i in range(len(profit)):
        #     jobs.append([startTime[i], endTime[i], profit[i]])

        # # Step 2: Sort the jobs based on their start time
        # jobs.sort(key=lambda x: x[0])
        # maxProfit = 0
        # maxVal = 0

        # pq = []

        # for start, end, profit in jobs:
        #     # Among all Overlapping options available
        #     # pop all non-overlapping intervals with curr
        #     # and extend curr with Most profitable Non-overlapping interval

        #     while pq and start >= pq[0][0]: # start >= end Non-overlap condi
        #         _, val = heappop(pq)
        #         maxVal = max(val, maxVal)
            
        #     # extend chain
        #     heappush(pq,(end, maxVal+profit))

        #     # loop invariant: After each iteration heap will have all overlapping interval chains

        #     maxProfit = max(maxProfit, maxVal+profit)
        # return maxProfit
        
        # # DP (Top-down) [Unintuitive]

        # # Step 1: Prepare the list of jobs (startTime, endTime, profit)
        # jobs = []
        # for i in range(len(profit)):
        #     jobs.append([startTime[i], endTime[i], profit[i]])

        # # Step 2: Sort the jobs based on their start time
        # jobs.sort(key=lambda x: x[0])

        # memo = {}

        # def findProfit(index):

        #     if index >= len(jobs):
        #         return 0

        #     if index in memo:
        #         return memo[index]
            
        #     nextIndex = bisect.bisect_left([job[0] for job in jobs], jobs[index][1])

        #     skipProfit = findProfit(index+1)

        #     includeProfit = jobs[index][2] + findProfit(nextIndex)

        #     maxProfit = max(skipProfit, includeProfit)
        
        #     # Memoize the result for this job index
        #     memo[index] = maxProfit

        #     return maxProfit

        # return findProfit(0)
        
        # [UINTUITIVE]DP Bottom UP :  We need to Calculate Last Job to First 
        # Memo :  Max Start_Time,  to the Smallest 

        # # Extract start times for binary search
        # startTime_sorted = [job[0] for job in jobs]
        
        # # Step 3: Initialize the memoization array for DP
        # n = len(jobs)
        # memo = [0] * n  # memo[i] will store the max profit starting from job i
        
        # # Step 4: Helper function to find the next job that doesn't conflict
        # def findNextJob(lastEndingTime):
        #     # Perform binary search to find the first job that starts after lastEndingTime
        #     idx = bisect.bisect_left(startTime_sorted, lastEndingTime)
        #     return idx
        
        # # Step 5: Dynamic Programming to calculate maximum profit with forward iteration
        # for i in range(n-1, -1, -1):  # Traverse from left to right (forward iteration)
        #     currProfit = jobs[i][2]  # Profit of the current job

        #     # Find the index of the first job that starts after the current job ends
        #     nextIndex = findNextJob(jobs[i][1])

        #     # If a non-conflicting job exists, add its profit to current job's profit
        #     if nextIndex < n:
        #         currProfit += memo[nextIndex]

        #     # Store the maximum of either:
        #     # - Profit by including the current job (currProfit)
        #     # - Profit by skipping the current job (memo[i-1]) (for i > 0)
        #     if i == n-1:
        #         memo[i] = currProfit
        #     else:
        #         memo[i] = max(currProfit, memo[i + 1])
        
        # # The answer will be in memo[n-1], which contains the max profit starting from job n-1
        # return memo[0]
        