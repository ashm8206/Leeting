class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:


        graph = defaultdict(list)
        for u, v, t in edges:
            graph[u].append((v, t))
            graph[v].append((u, t))

        # minimize the passingFees
        # travel in maxTime  ==> sum of wt  else -1

        src = 0
        dest = len(passingFees) - 1
        pq = [(passingFees[0], 0,  src)] # cost, time, node

        # visited tracks best times to reach each node
        # < maxTime
        visited = {}

        while pq:
            cost, time, node = heapq.heappop(pq)

            if time > maxTime:
                continue
            
            if node == dest:
                return cost

            # skip if we've been here with lesser or equal
            if node in visited and visited[node] <= time:
                continue
        
            visited[node] = time

            for nei, nei_t in graph[node]:
                heapq.heappush(pq, (cost + passingFees[nei], time + nei_t, nei))

        return -1
        