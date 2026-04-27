class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph = defaultdict(list)
        for u, v, wt in flights:
            graph[u].append((v, wt))

        # (cost, stops, node)
        pq = [(0, 0, src)]

        # visited tracks best stops to reach each node
        # (fewer stops = more flexibility remaining)
        visited = {}

        while pq:
            cost, stops, node = heapq.heappop(pq)

            if node == dst:
                return cost

            # skip if we've been here with fewer or equal stops
            if node in visited and visited[node] <= stops or stops > k:
                continue
            visited[node] = stops

            for nei, nei_wt in graph[node]:
                heapq.heappush(pq, (cost + nei_wt, stops + 1, nei))

        return -1


