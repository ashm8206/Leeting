class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        n = len(graph) - 1
        res = []
        def backtrack(node, path):
            
            path.append(node)
            
            if node == n:
                res.append(path[:])
            
            for next_node in graph[node]:
                backtrack(next_node,path)
                path.pop()
        
        backtrack(0,[])
        return res
                
