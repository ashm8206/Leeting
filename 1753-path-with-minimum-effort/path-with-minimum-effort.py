import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

    

        #Shortest path in a weighted Graph
        #https://leetcode.com/problems/shortest-path-in-binary-matrix/
        m, n = len(heights), len(heights[0])

        dist = [[math.inf] * n for _ in range(m)]
        dist[0][0] = 0
        
        minHeap = [(0, 0, 0)] # distance, row, col
        DIR = [(0,1),(1,0),(-1,0),(0,-1)]
        # seen = set((0,0))
        ans = 0

        while minHeap:
            d, r, c = heapq.heappop(minHeap)
            if d > dist[r][c]:
                continue
                # we dnt use this
        
            
            if r == m - 1 and c == n - 1:
                return d  # Reach to bottom right
            
            for dx, dy in DIR:
                nr, nc = r + dx, c + dy
                if 0 <= nr < m and 0 <= nc < n:
                    newDist = max(d, abs(heights[nr][nc] - heights[r][c]))
                    if dist[nr][nc] > newDist:
                        dist[nr][nc] = newDist
                        heappush(minHeap, (dist[nr][nc], nr, nc))