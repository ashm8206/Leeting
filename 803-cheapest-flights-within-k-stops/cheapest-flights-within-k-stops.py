from collections import defaultdict
import heapq
import copy
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = defaultdict(list)

    def addEdge(self,u,v, wt):
        self.adj_list[u].append((v,wt))

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        

        #  Bellman

        # Distance from source to all other nodes.
        # dist = [2**31 for i in range(n)]
        # dist[src] = 0

        # # Run only K+1 times since we want shortest distance in K hops. --> In bellman we run once more to compute shortest distnace with edge
        # for i in range(k+1):
        #     #Create a copy of dist vector.
        #     temp = copy.deepcopy(dist)

        #     for flight in flights: 
        #         if (dist[flight[0]] != 2**31):
        #             temp[flight[1]] = min(temp[flight[1]], dist[flight[0]] + flight[2])
                
            
        #     #Copy the temp vector into dist.
        #     dist = temp
        
        # return -1 if dist[dst] == 2**31 else dist[dst]
    


        # Cheapest flights
        # flight with lower cost
        # flight with lower stops. i.e we track 

        g = Graph(n)

        for start, end, wt in flights:
            g.addEdge(start,end,wt)
        
        pq = [(0,0,src)]

        visited = { i: 2**31 for i in range(n)}
        visited[src] = 0

        while pq:
    
            curr_wt, curr_stops, node = heapq.heappop(pq)

            if visited[node] < curr_stops or curr_stops > k + 1:
                continue

            visited[node] = curr_stops  

            if node == dst:
                return curr_wt

            
            for nei, nei_wt in g.adj_list[node]:
                
                heapq.heappush(pq,(nei_wt+curr_wt, curr_stops+1, nei))
    
        return -1



