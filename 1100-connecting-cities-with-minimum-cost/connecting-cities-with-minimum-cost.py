from collections import defaultdict
import heapq
class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        
        adjList = defaultdict(list)
    
        for u, v , w in connections:
            adjList[u].append((w, v))
            adjList[v].append((w, u))

        
    
   
        src = 1
        pq = []
        heapq.heappush(pq,(0,src))

        visited = set()

        ans = 0
        while pq and len(visited) < n:
            wt, city = heapq.heappop(pq)

            if city not in visited:
                visited.add(city)
                ans+= wt

                for nei_wt, nei in adjList[city]:
                        heapq.heappush(pq, (nei_wt, nei))

        return ans  if len(visited)==n else -1
