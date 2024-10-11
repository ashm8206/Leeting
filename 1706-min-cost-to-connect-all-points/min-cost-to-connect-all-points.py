class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjList = defaultdict(list)

        n = len(points)

        for i in range(n):
            adjList[tuple(points[i])].extend(points[:i]+ points[i+1:])
        
        visited = set()
        pq = [(0, tuple(points[0]))] # arbitary pt
        
        ans = 0
        while pq and len(visited) < n:
            cost, pt = heapq.heappop(pq) # this pt gotta be tupple

            if pt not in visited:
                visited.add(pt)
                ans+= cost

                for nei in adjList[pt]:
                    x1, y1 = pt
                    x2, y2 = nei
                    cost = abs(x1-x2)+ abs(y1-y2)
                    heapq.heappush(pq, [cost, tuple(nei)])
        
        return ans if len(visited) == n else -1