class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        # Method I : O(nlogn), space (O(n))-->Large arrays or O(1) --> small arrays
    
        n = len(intervals)
        if n <= 1:
            return True

        intervals.sort(key = lambda x:x[0])

        for i in range(1,n):
            s1, e1 = intervals[i-1]
            s2, e2 = intervals[i]
            if s2 < e1:
                return False
        return True

    
        