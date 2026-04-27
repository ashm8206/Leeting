from collections import defaultdict
class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        graph = defaultdict(list)
        for highway in highways:
            u, v, toll = highway
            graph[u].append((v, toll))
            graph[v].append((u, toll))
        
        pq = [] # cost, city, discounts
        heapq.heappush(pq, (0, 0, discounts))

        visited = dict()
        while pq:
            wt, city, discounts_used = heapq.heappop(pq)

            if city == n - 1:
                return wt

             # skip if already found cheaper path and don't have extra discounts
            if city in visited and discounts_used <= visited[city]:
                continue
            
            # found a better option
            visited[city] = discounts_used

           
            
            for nei, nei_wt in graph[city]:
                # push with and without it discounted
                if discounts_used > 0: # add both
                    heapq.heappush(pq, (nei_wt // 2 + wt, nei, discounts_used - 1 ))            
                heapq.heappush(pq, (nei_wt + wt, nei, discounts_used ))
        
        return -1

