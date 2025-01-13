class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:


        counts = Counter(tasks)

        maxHeap = [(-v, k) for k, v in counts.items()]
        heapq.heapify(maxHeap)

        queue = deque()
        time = 0
        while maxHeap or queue:
            time+=1

            if maxHeap:
                cnt, key = heapq.heappop(maxHeap)
                cnt+=1 # reduces count
                if abs(cnt) > 0:
                    queue.append([time+n, cnt, key])
            
            if queue and queue[0][0]==time:
                _, cnt, key = queue.popleft()
                heapq.heappush(maxHeap, (cnt, key))
        return time




        
        # # https://www.youtube.com/watch?v=s8p8ukTyA2I
        # counts = Counter(tasks)

        # maxHeap = [ -cnt for k, cnt in counts.items()]
        # heapq.heapify(maxHeap)

        # q = deque() # we add the tasks which are made to wait
        # time = 0

        # # print(maxHeap)
        # while maxHeap or q:
        #     time +=1

        #     if maxHeap:
        #         cnt = heapq.heappop(maxHeap)
        #         cnt+=1
        #         # since numbers re -ve 1+ reduces count by 1,-1
       
        #         if cnt!=0:
        #             q.append([cnt,time+n]) #CountRemain, timeItsAvailableAgain)
                
        #     if q and q[0][1]==time:
        #         heapq.heappush(maxHeap, q.popleft()[0]) # add remian cnts again
        
        # return time

