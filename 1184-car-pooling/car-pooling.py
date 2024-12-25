class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        events = []

        for cap, s, e in trips:
            events.append((s, 1, cap))
            events.append((e, -1, cap))
        
        events.sort()

        curr_sum = 0
        for t, cmd, cap in events:
            if curr_sum > capacity:
                return False
            
            if cmd > 0:
                curr_sum += cap
            else:
                curr_sum -= cap
        return True
