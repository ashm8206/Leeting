# from functools import lru_cache

# @lru_cache(maxsize=None)
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
       
        def bfs(r, c, m, n):
            # In every bfs you have the visit the previous cells
            seen = set()
            q = deque([(r, c, 0)])
            
            while q:
                r, c, d = q.popleft()
               
                for dx, dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                    nr = r + dx
                    nc = c + dy

                    if 0 <= nr < m and 0 <= nc < n:
                         if (nr,nc) not in seen and grid[nr][nc]==0:
                            seen.add((nr, nc))
                            #q.append((nr,nc,d+1))
                            q.append((nr, nc, d+1))
                            distance[(nr, nc)].append(d+1)


        m , n = len(grid), len(grid[0])
        total_buildings = 0

        distance = collections.defaultdict(list)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    total_buildings+=1
                    bfs(i,j, m, n)

        # print(distance)
        minimum = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    if (i, j) in distance and len(distance[(i, j)]) == total_buildings:
                        #print(dist[i][j])
                        minimum = min(minimum, sum(distance[(i, j)]))
        return minimum if minimum != float('inf') else -1

                        



        