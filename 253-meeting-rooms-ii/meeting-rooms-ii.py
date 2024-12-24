import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        events = SortedList()
    
        # Add start and end events
        for start, end in intervals:
            events.add([start, 1])
            events.add([end, -1])
    
        rooms = 0
        max_rooms = 0
        
        # Process events in chronological order
        for _, event_type in events:
            rooms += event_type
            max_rooms = max(max_rooms, rooms)
        
        return max_rooms


        # events = SortedDict()
        # maxRoomCount = 1 # atleast one interval

        # for s, e in intervals:
        #     events[s] = events.get(s, 0) + 1
        #     events[e] = events.get(e, 0) - 1
        
        # # 1, 13
        # count = 0
        # for time, val in events.items():
        #     count+= val
        #     if count > 1:
        #         maxRoomCount = max(maxRoomCount,count)
        
        # return maxRoomCount

        # Method II
        # free_rooms = []
        # intervals.sort(key = lambda x: x[0])

        # heapq.heappush(free_rooms, intervals[0][1]) # ending time
        
        # n = len(intervals)

        # for i in range(1,n):
        #     s2, e2 = intervals[i]
        #     if free_rooms and s2 >= free_rooms[0]: 
        #             heapq.heappop(free_rooms)
        #             heapq.heappush(free_rooms, e2)
        #     else:
        #         # Empty Heap or  Meeting has start time  < end time of First
        #         # Just push
        #         heapq.heappush(free_rooms, e2)
        # return len(free_rooms)

        
        

