class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        def prims(edges, forced_edge=None):

            visited = set()
            adjList = defaultdict(list)

            for u, v, w in edges:
                adjList[u].append((v, w))
                adjList[v].append((u, w))
            
            weight = 0
            pq = []

            if forced_edge is not None:
                u, v, w = edges[forced_edge]
                # Forcefully Include this Edge
                visited.add(u)
                visited.add(v)
                weight += w
                for nxt, w in adjList[u]:
                    heapq.heappush(pq, (w, nxt))
                for nxt, w in adjList[v]:
                    heapq.heappush(pq, (w, nxt))
            else:
                heapq.heappush(pq, (0, 0))
                # start with edge 0, wt 0

            while pq and len(visited) < n:
                wt, node = heapq.heappop(pq)
                if node not in visited:
                    visited.add(node)
                    weight+=wt

                    for nxt, nxt_wt in adjList[node]:
                        # if nxt not in visited:
                        heapq.heappush(pq, (nxt_wt, nxt))
           
            return weight if len(visited)==n else float("inf")
            


        # Find the weight of the original MST
        mst_weight = prims(edges)
        # print(mst_weight)
        
        criticals, pseudo_criticals = [], []

        for i in range(len(edges)):
            new_weight = prims(edges[:i] + edges[i+1:])
            if new_weight > mst_weight:
                criticals.append(i)
        
        for i in range(len(edges)):
            if i not in criticals:
                new_weight = prims(edges, i)
                if new_weight == mst_weight:
                    pseudo_criticals.append(i)

        return [criticals, pseudo_criticals]
