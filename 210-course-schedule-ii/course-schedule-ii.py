from collections import defaultdict #, deque
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjList = defaultdict(list)
        self.indegree = [0]*self.vertices
    
    def addEdge(self, u, v):
        self.adjList[u].append(v)
        self.indegree[v]+=1
    
#     def __init__(self, vertices):
#         self.graph = defaultdict(list)
#         self.vertices = vertices
#         self.inDeg = [0] * vertices
    
#     def addEdge(self, u, v):
#         self.graph[u].append(v)
#         self.inDeg[v] += 1 #class attri, @toplogical ordering

 
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
            graph = Graph(numCourses)

            coursesOrder = []
            for end, start in prerequisites:
                graph.addEdge(start, end)
            
            coursesNoPreq = [ idx for idx, ideg in enumerate(graph.indegree)if ideg==0]
            coursesNoPreq = deque(coursesNoPreq)

            # visited= set()
            while coursesNoPreq:
                courseToTake = coursesNoPreq.popleft()
                coursesOrder.append(courseToTake)

                for nei in graph.adjList[courseToTake]:
                    # if nei not in visited: 
                        # Don't add nei, already in queue to queue again
                        # These will be  marked as visited.
                        graph.indegree[nei]-=1
                        if graph.indegree[nei] == 0: 
                            coursesNoPreq.append(nei)
                            # visited.add(nei)
            return coursesOrder if len(coursesOrder) == numCourses else []

#             for end, start in prerequisites:
#                 graph.addEdge(start,end)

#             noIdegNodes = [idx for idx, course in enumerate(graph.inDeg) if course == 0]
#             noIdegNodes = deque(noIdegNodes)
#             coursesOrder = []
#             # Cycles
#             visited = set()
#             while len(noIdegNodes) > 0:
#                 courseToTake = noIdegNodes.popleft()

#                 if courseToTake not in visited:
#                     visited.add(courseToTake)
#                     for nei in graph.graph[courseToTake]:
#                         graph.inDeg[nei] -= 1

#                         if graph.inDeg[nei] == 0:
#                             noIdegNodes.append(nei)
#                     coursesOrder.append(courseToTake)
#                     if len(coursesOrder) == numCourses:
#                         return coursesOrder
#             return []
                    