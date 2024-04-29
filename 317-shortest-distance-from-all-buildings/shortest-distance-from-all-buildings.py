# from functools import lru_cache

# @lru_cache(maxsize=None)
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        # My method is Correct But TLE
        # minDist = 2**31
        # m = len(grid)
        # n = len(grid[0])

        # def bfs(r, c, buildings):
        #     q = collections.deque()
        #     visited = set()
            
        #     q.append((r,c,0))
        #     visited.add((r,c))
        #     # print(r, c)
        #     # print("*****")
        #     dist = 0
        #     numBuildings = 0
        #     while q and numBuildings!=buildings:
        #         r, c, level = q.popleft()

        #         for nr, nc in [(r+1,c),(r-1,c),(r,c-1),(r,c+1)]:
        #             if 0<=nr<m and 0<=nc<n and (nr,nc) not in visited:
        #                 if grid[nr][nc]==1:
        #                     numBuildings+=1
        #                     dist+= level + 1
        #                     # print(dist, nr, nc)
        #                 elif grid[nr][nc]==0:
        #                     q.append((nr,nc, level+1))
                        
        #                 visited.add((nr,nc))
                        
        #     return dist if numBuildings==buildings else -1


        # def getNumBuildings(grid):
        #     numBuildings = 0 
        #     for r in range(m):
        #         for c in range(n):
        #             if grid[r][c]==1:
        #                 numBuildings+=1
        #     return numBuildings

        # buildings = getNumBuildings(grid)
        
        # # print(bfs(0,1,3,set()))
        # # Start BFS from every land
        # # print(buildings)
        # for r in range(m):
        #     for c in range(n):
        #         if grid[r][c]==0:
        #             curr_dist = bfs(r,c, buildings)

        #             if curr_dist!=-1:
        #                 # All Buildings can be reached from this empty land
        #                 minDist = min(minDist,curr_dist)
        
        # return minDist if minDist < 2**31 else -1

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

        #print(dist)
        minimum = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    if (i, j) in distance and len(distance[(i, j)]) == total_buildings:
                        #print(dist[i][j])
                        minimum = min(minimum, sum(distance[(i, j)]))
        return minimum if minimum != float('inf') else -1

                        



        