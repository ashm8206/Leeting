import heapq
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = defaultdict(list)

    def addEdge(self,u,v, wt):
        self.adj_list[u].append((v,wt))
        self.adj_list[v].append((u,wt))

class Solution:

    
    
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        graph = Graph(n)

        for (s, e), prob in zip(edges, succProb):
            graph.addEdge(s,e, prob)
            graph.addEdge(e,e, prob)

        
        max_prob = [0.0]*n
        max_prob[start_node] = 1.0 # already reached here 
        # same as 0 in minDist calculation

        pq = [(-1.0, start_node)] # minHeap

        # visited = set() # undirected graph thats why

        while pq:
            prob, node = heapq.heappop(pq)
            
            prob *= -1
         

            if max_prob[node] > prob:
                continue

            # visited.add(node)
            # if node==end_node:
            #     return -prob
            
            for nei, path_prob in graph.adj_list[node]:
                # if nei not in visited:
                if prob * path_prob > max_prob[nei]:
                    max_prob[nei] = prob * path_prob
                    heapq.heappush(pq, (-max_prob[nei], nei))
        return max_prob[end_node]
            






