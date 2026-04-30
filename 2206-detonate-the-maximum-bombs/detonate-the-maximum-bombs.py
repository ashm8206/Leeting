class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n, ans, graph = len(bombs), 0, defaultdict(list)

        # Build Graph

        for i in range(n):
            for j in range(i+1, n):

                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                dist = (x1-x2)**2 + (y1-y2)**2
                if dist <= r1 ** 2: # does this distance lie in i1 radius?
                    graph[i].append(j)
                if dist <= r2**2: # does this distance lie in J1 radius?
                    graph[j].append(i)


        def dfs(node: int, visited: set = None) -> set:
        
            island_size = 1
            for child in graph[node]:
                if child not in visited:
                    visited.add(child)
                    island_size+=dfs(child, visited)

            return island_size

        for i in range(n):
            island_size = dfs(i, {i})
            ans = max(ans, island_size)
                          
        return ans