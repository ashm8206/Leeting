"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # Line Sweep
        events = []

        for emp in schedule:
            for iv in emp:
                
                events.append((iv.start, 1))
                events.append((iv.end, -1))
        
        
        events.sort()
     
        count = 0
        start = -1
        res = []

        for end, val in events:
            if count == 0 and start >= 0 and end-start > 0 :
                res.append(Interval(start,end))
            count += val

            if count==0:
                start = end
        return res



        # Solve After Non-Overlapping Interval 493
        # ans = []
        # intervals = []

        # # Merging all the employee schedules into one list of intervals
        # for s in schedule:
        #     # flatten and append
        #     intervals.extend(s)
        

        # # Sorting all intervals
        # intervals.sort(key=lambda x: x.start)
        # # Initializing prev_end as the endpoint of the first interval
        # prev_end = intervals[0].end
        # # iterating through the intervals and adding the gaps we find to the answer list
        # for interval in intervals:
        #     if interval.start > prev_end:
        #         ans.append(Interval(prev_end, interval.start))
        # # if the current interval's ending time is later than the current prev_end, update it
        #     prev_end = max(prev_end, interval.end)
        # return ans