class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        #  Hashmap? 0 .. n-1 # Friend:Index
        hm = {i:tup for i, tup in enumerate(times)}
        shm = sorted(hm.items(), key = lambda x: x[1][0])
       
    
        occupied = []
        minUnoccupied = []
        nextChair = 0

        for friend, time in shm:
            arr, leav = time

            while occupied and arr >= occupied[0][0]:
                _, chairNum = heapq.heappop(occupied)
                heapq.heappush(minUnoccupied, chairNum)

            if minUnoccupied:
                chairNum = heapq.heappop(minUnoccupied)
            else:
                chairNum = nextChair
                nextChair = chairNum + 1
                
            heapq.heappush(occupied, (leav, chairNum))
    
            if friend == targetFriend:
                return chairNum
        return -1


          