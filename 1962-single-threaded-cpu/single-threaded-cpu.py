class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        res = []
        tasks = sorted([(t[0],t[1], i) for i, t in enumerate(tasks)])
        i = 0
        n = len(tasks)
        h = []
        time = tasks[0][0]

        while len(res) < n:
            while i < n and tasks[i][0] <=time:
                heapq.heappush(h, (tasks[i][1], tasks[i][2])) 
                # processing and original index
                i+=1
            if h:
                processing_time, idx = heapq.heappop(h)
                time+=processing_time
                res.append(idx)
            else:
                
                time = tasks[i][0]
        return res

