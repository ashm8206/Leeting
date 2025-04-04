class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        # Create events for sorting and processing
        events = []
        
        # Create events for intervals:
        # For each interval, create a start event (type 0) and end event (type 2)
        for idx, (start, end) in enumerate(intervals):
            interval_size = end - start + 1
            events.append((start, 0, interval_size, idx))  # Start event
            events.append((end, 2, interval_size, idx))    # End event
        
        # Create events for queries (type 1)
        for i, query_point in enumerate(queries):
            events.append((query_point, 1, i))
        
        # Sort all events by:
        # 1. Time (ascending)
        # 2. Type (process ends before queries for the same time)
        events.sort(key=lambda x: (x[0], x[1]))
        
        # Min heap to store active intervals as (size, index) pairs
        sizes = []  
        
        # Initialize answer array with -1 (for queries with no containing interval)
        ans = [-1] * len(queries)
        
        # Track which intervals have ended but haven't been removed from the heap yet
        inactive = [False] * len(intervals)
        
        # Process all events in order
        for time, event_type, *rest in events:
            if event_type == 0:  # Interval start
                interval_size, idx = rest
                # Add interval to the min heap
                heapq.heappush(sizes, (interval_size, idx))
                
            elif event_type == 2:  # Interval end
                idx = rest[1]
                # Mark interval as inactive (lazy deletion)
                inactive[idx] = True
                
            else:  # Query
                query_idx = rest[0]
                # Remove any inactive intervals from the top of the heap
                while sizes and inactive[sizes[0][1]]:
                    heapq.heappop(sizes)
                    
                # If there are any active intervals, the smallest one is at the top of the heap
                if sizes:
                    ans[query_idx] = sizes[0][0]  # Store the size of the smallest interval
        
        return ans



        # elegant

        # q = sorted([q,i] for i, q in enumerate(queries))
        
        # intervals.sort(key = lambda x: x[1]-x[0])

        # output = [-1] * len(queries)

        # for start, end in intervals:
        #     ind = bisect.bisect(q, [start])
        #     while ind < len(q) and q[ind][0]<=end:
        #         output[q.pop(ind)[1]] = end-start+1

        # return output