from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int: 
    
        # Lets be Vanilla, create a defaulist(list) --> graph start at all keys 
        #traverse neigbors the number of times you come up, increment the count
        
        # do a bfs, O(V)

        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        color_map = defaultdict(list)

        
        def dfs(u, color):
            
            seen.add(u)
            color_map[color].append(u)
            for nei in graph[u]:
                if nei not in seen:
                    dfs(nei,color)
        count = 0
        seen = set()
        color = 0
        for u in range(n):
            
            if u not in seen:
                dfs(u, color)
                count+=1
                color+=1
    
        # print(color_map)
        return count
