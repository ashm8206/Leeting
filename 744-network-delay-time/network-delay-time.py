from collections import defaultdict
import heapq

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = defaultdict(list)
        
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # HEAP Solution
        #Time : O(N) --> dist calculation
        #     : E O(logE) --> all edges
        # but E = N(N-1) --> N**2
        # So    E 2*O(LOG N) -> ELOGN --> N2logN

        #Dijskta. -> Tighter bound, only adding vertices selctively that follow
        #D[curr] + wt ( curr to nei) = D[nei]
        # Time: O(N)-> dist calculation
        #.    : NLOGN

        # Both cases : Space complexity is the same.

        ####-----HEAP---####

        # g = Graph(n)
        # visited = {}
        
    
        # for start, end, weight in times:
        #     g.adj_list[start].append((end,weight))
        
        # pq = [(0,k)]
        
        # while pq:
        #     print(pq)
        #     elapsed_time, node = heapq.heappop(pq)
        #     if node not in visited:
        #         visited[node] = elapsed_time
        #         for nei, wt in g.adj_list[node]:
        #             if nei not in visited:
        #                 heapq.heappush(pq,(elapsed_time + wt,nei))
        
        # return max(visited.values()) if len(visited) == n else -1


        ### DIJSKSTRAS

        g = Graph(n)
        visted =  { i: 2**31 for i in range(1,n+1)} # V.IMP # visited +distance array

        for start, end, weight in times:
            g.adj_list[start].append((end,weight))

        pq = [(0,k)] #K --> Source
        visted[k] = 0

        while pq:
            currDist, currNode = heapq.heappop(pq)
            
            for nei, wt_to_nei in g.adj_list[currNode]:
                # if visit to neigh = optimal_visit_time_curr_node +  wt(curr_node, nei)
                if visted[nei] > visted[currNode] + wt_to_nei:
                    visted[nei] = visted[currNode] + wt_to_nei
                    heapq.heappush(pq,(visted[nei],nei))
        
        return  -1 if max(visted.values()) == 2**31 else max(visted.values())
        
        
            
        
            
        