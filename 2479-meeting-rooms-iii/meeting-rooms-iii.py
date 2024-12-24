class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # 1. Sort Meeting by start time
        # 2. Till we have meeting:
        #      
        #.    Iterative over all rooms: (end time, idx)
        #           if start_time >= room[i]:
        #               asign
        #.       Also have Hashmap ; count asignment 

        meetings.sort(key= lambda x : x[0])
        meeting_rooms = [0] * n  # with their end times
        meeting_counts = [0]* n # this is the count
 

        for s, e in meetings:
            minEndTime = 10**10
            nextRoomIdx = 0
            foundRoom = False

            for i in range(n):
                # for room in meeting rooms:

                if s >= meeting_rooms[i]:
                    meeting_rooms[i] = e 
                    # didnt have to wait, so time is pushed not duration
                    meeting_counts[i]+=1
                    foundRoom = True
                    break # done, break from looping rooms
                
                if meeting_rooms[i] < minEndTime:
                    minEndTime = meeting_rooms[i]
                    nextRoomIdx = i
            # else:
            if not foundRoom:
                meeting_rooms[nextRoomIdx] += e-s # duration 
                # add duration incase it gets pushed back
                meeting_counts[nextRoomIdx]+=1
            
     
        return meeting_counts.index(max(meeting_counts))

                

