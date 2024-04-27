class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

            # i=0
            # end=1
            # start=0
            # merged=[] # monotonic Array
            
            # # find position of new interval, skip/append to new list all intervals
            # # whose end time < new_interval_start time
            # while i < len(intervals) and intervals[i][start] < newInterval[start]:
            #     merged.append(intervals[i])
            #     i+=1

            # # merge / append new interval

            # if merged and merged[-1][end] >= newInterval[start]:
            #     newInterval[start] = min(merged[-1][start],newInterval[start])
            #     newInterval[end] = max(merged[-1][end],newInterval[end])
            #     merged.pop()
            # merged.append(newInterval)

            # # add all the remaining intervals to the output
            # while i < len(intervals):

            #     if merged and merged[-1][end] >= intervals[i][start]:
            #         intervals[i][start] = min(merged[-1][start],intervals[i][end])
            #         intervals[i][end] = max(merged[-1][end],intervals[i][end])
            #         merged.pop()
                
            #     merged.append(intervals[i])
            #     i += 1
            # #print(i)
            # return merged

            if not intervals:
                return [newInterval]
            
            target = newInterval[0]
            left = 0
            right = len(intervals)

            insert_idx = bisect.bisect(intervals,[target])
            
            intervals.insert(insert_idx, newInterval)
            # Inserting this might need but one previous to be merged
            # Following the insert to be merged
            # print(intervals)
            merged = []
            for interval in intervals:
                if merged and interval[0] <= merged[-1][1]:
                    start = merged[-1][0] # we did BS so the start remains same
                    new_end = max(merged[-1][1], interval[1])
                    merged.pop()
                    merged.append([start,new_end])
                else:
                    merged.append(interval)
                
            return merged

        


            return []

