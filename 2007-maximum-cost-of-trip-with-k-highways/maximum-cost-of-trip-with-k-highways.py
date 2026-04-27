class Solution:
    def maximumCost(self, n: int, highways: List[List[int]], k: int) -> int:
        
    
        graph = defaultdict(list)
        for u, v, toll in highways:
            graph[u].append((v, toll))
            graph[v].append((u, toll))

        visited = set()
        best = [-1]

        @lru_cache(maxsize = None)
        def dfs(city, steps, cost):
            if steps == k:
                best[0] = max(best[0], cost)
                return

            for nei, toll in graph[city]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei, steps + 1, cost + toll)
                    visited.remove(nei)    # ← backtrack, like string_search!

        for start in range(n):
            visited.add(start)
            dfs(start, 0, 0)
            visited.remove(start)

        return best[0]