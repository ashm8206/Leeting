
from heapq import heappush, heappop
class Solution:
    def getSkyline(self, buildings):
       
        # Bigger heights need to process first
        # choose from K heights

        events = [(l, -h, r) for l, r, h in buildings]
        events+= [(r, 0, 0) for _,r,_ in buildings]
        events.sort()

    
        pq = [(0, float('inf'))]  # (height, end_x)
        # Initialize priority queue with ground level
        # (0,float('inf')) represents ground level extending infinitely 

        res = []

        for l, h, r in events:
            while pq and pq[0][1] <= l:
                heappop(pq)
            
            if h: # h!=0
                heappush(pq, (h, r))

            # print(pq, res, l)

            if not res or (res and res[-1][1] != -pq[0][0]):
                res.append([l, -pq[0][0]])

        return res
            


        # # Create events: (x, height)
        # events = [(l, -h, r) for l, r, h in buildings]
        # events += list({(r, 0, 0) for _, r, _ in buildings})

        # events.sort()
        
        # # Process events
        # heap = [(0, float('inf'))]  # (height, end_x)
        # res = []
        
        # for x, h, r in events:
        #     # Remove ended buildings
        #     while heap[0][1] <= x:
        #         heappop(heap)
            
        #     # Add new building
        #     if h:
        #         heappush(heap, (h, r))
            
        #     # Update skyline if height changes
        #     if not res or res[-1][1] != -heap[0][0]:
        #         res.append([x, -heap[0][0]])
                
        # return res

        