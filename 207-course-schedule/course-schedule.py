from collections import defaultdict, deque
class Graph:
    def __init__(self, vertices):
        self.edges = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices
        self.indegree = [0]*vertices
 
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.edges[u].append(v)
 
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = Graph(numCourses)

        for end, start in prerequisites:
            graph.addEdge(start,end)
            graph.indegree[end]+=1

        node_with_zero_indegree = [idx for idx,course in enumerate(graph.indegree) if course == 0 ]

        coursesTaken =[]
        visited = set()
        q  = deque(node_with_zero_indegree)
        
        while q:
            curr = q.popleft()

            for nei in graph.edges[curr]:
                graph.indegree[nei] -= 1
                if graph.indegree[nei] == 0:
                    q.append(nei)
            coursesTaken.append(curr)
            if len(coursesTaken) == numCourses:
                return True
        return False


