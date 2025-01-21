class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # pq = [(abs(arr[i]-x),arr[i]) for i in range(k)]
     
        # for num in arr[k:]:
        #     if len(pq) > k:
        #         heapq.heappop(pq)
         
        #     heapq.heappush(pq,(abs(num-x),num))
        # print(pq)

        h = []
    
        for n in arr:
            if len(h) < k:
                heapq.heappush(h, n)
            elif abs(n-x) < abs(h[0]-x):
                heapq.heappushpop(h, n)
    
        return sorted(h)

        res = []
        # while len(res) < k:
        #     _, num =heapq.heappop(pq)
        #     res.append(num)
        # res.sort()
        # #print(res)
        return res