class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:

       
        # Find first and last meeting start times
        last = max(meeting[0] for meeting in meetings)
        first = min(meeting[0] for meeting in meetings)
        last += 1
        
        # Timeline of meeting end times
        end = [-1] * last
        for start, end_time in meetings:
            end[start] = end_time
        
        # Track when each room is busy until and meeting count
        busy = [0] * n  # room i is busy until busy[i]
        count = [0] * n  # room i had count[i] meetings
        
        # Line sweep through timeline
        for i in range(first, last):
            if end[i] > -1:  # If there's a meeting starting at time i
                found = False
                
                # Try to find an available room
                for room in range(n):
                    if busy[room] <= i:
                        busy[room] = end[i]
                        count[room] += 1
                        found = True
                        break
                
                # If no room immediately available, use the one that becomes free first
                if not found:
                    next_room = busy.index(min(busy))
                    busy[next_room] += end[i] - i
                    count[next_room] += 1
        
        # Return room with most meetings
        return count.index(max(count))

        # # 1. Sort Meeting by start time
        # # 2. Till we have meeting:
        # #      
        # #.    Iterative over all rooms: (end time, idx)
        # #           if start_time >= room[i]:
        # #               asign
        # #.       Also have Hashmap ; count asignment 

        # meetings.sort(key= lambda x : x[0])
        # meeting_rooms = [0] * n  # with their end times
        # meeting_counts = [0]* n # this is the count
 

        # for s, e in meetings:
        #     minEndTime = 10**10
        #     nextRoomIdx = 0

        #     for i in range(n):
        #         # for room in meeting rooms:

        #         if s >= meeting_rooms[i]:
        #             meeting_rooms[i] = e 
        #             # didnt have to wait, so time is pushed not duration
        #             meeting_counts[i]+=1
           
        #             break # done, break from looping rooms
                
        #         if meeting_rooms[i] < minEndTime:
        #             minEndTime = meeting_rooms[i]
        #             nextRoomIdx = i
        #     else:
          
        #         meeting_rooms[nextRoomIdx] += e-s # duration 
        #         # add duration incase it gets pushed back
        #         meeting_counts[nextRoomIdx]+=1
            
     
        # return meeting_counts.index(max(meeting_counts))

                

