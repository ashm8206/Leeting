class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        n = len(intervals)

        intervals = sorted(intervals,key=lambda x: x[0])
        result = []
        if n == 1:
            return intervals
        else:
            result.append(intervals[0])

        for start, end in intervals:
            if result and start <= result[-1][1]:
                # keep processing the stack
                new_start = min(result[-1][0], start)
                new_end = max(result[-1][1], end)
                result.pop()
                result.append([new_start, new_end])
            else:
                result.append([start,end])
        return result



        # Line-Sweep
        count = 0
        events = SortedList()
        res = []

        for s, e in intervals:
            events.add((s,1))
            events.add((e,-1))

        n = len(events)
        start = -1

        print(events)
        for i in range(n):
            if count == 0:
                start = events[i][0]
            count += events[i][1]
            if count == 0:
                if res and res[-1][1]== start:
                    res[-1] = [min(res[-1][0], start), max(res[-1][1], events[i][0])]
                else:
                    res.append([start, events[i][0]])
        return res

                
           