class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

            # Linear Scan

            n = len(intervals)
            if n == 0:
                return [newInterval]
            
            i = 0
            res = []

            # # Case 1: No overlapping before merging intervals
            #  curr_end < new_start
            while i < n and intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
                i += 1
            # curr_start <= new_end
            # Case 2: Overlapping and merging intervals
            # s2 <= e1
            while i < n and  intervals[i][0] <= newInterval[1]:
                
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
                i += 1
            res.append(newInterval)

            while i < n:
                res.append(intervals[i])
                i += 1

            return res

            # # Line Sweep:
            # count = 0
            # events =  []  # or SortedList
            # res = []

            # for s, e in intervals + [newInterval]:
            #     # events.add((s,1))
            #     # events.add((e,-1))
            #     events.append((s,1))
            #     events.append((e,-1))
                

            # events.sort()

            # n = len(events)
            # start = -1

            # for i in range(n):
            #     if count == 0:
            #         start = events[i][0]

            #     count += events[i][1]
            #     if count == 0:
            #         if res and res[-1][1]== start:
            #             res[-1] = [min(res[-1][0], start), max(res[-1][1], events[i][0])]
            #         else:
            #             res.append([start, events[i][0]])
            # return res
                

            

            
            # # Case 3: No overlapping after merging newInterval
            

            # BS
            # if not intervals:
            #     return [newInterval]
            
            # target = newInterval[0]
            # left = 0
            # right = len(intervals)

            # insert_idx = bisect.bisect(intervals,[target])
            
            # intervals.insert(insert_idx, newInterval)
            # # Inserting this might need but one previous to be merged
            # # Following the insert to be merged
            # # print(intervals)
            # merged = []
            # for interval in intervals:
            #     if merged and interval[0] <= merged[-1][1]:
            #         start = merged[-1][0] # we did BS so the start remains same
            #         new_end = max(merged[-1][1], interval[1])
            #         merged.pop()
            #         merged.append([start,new_end])
            #     else:
            #         merged.append(interval)
                
            # return merged
