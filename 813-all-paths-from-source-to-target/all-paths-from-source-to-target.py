class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        n = len(graph) - 1 
        # ending node
        res = []



        
        def backtrack(slate, node):

            if node == n: 
                res.append(slate[:])
                return


            for next_node in graph[node]:
                slate.append(next_node)
                backtrack(slate, next_node)
                slate.pop()
            
          
        
        backtrack([0], 0)
        return res
                
