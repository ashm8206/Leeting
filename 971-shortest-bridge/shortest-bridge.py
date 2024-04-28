from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    firstIsland_x, firstIsland_y = i, j
                    break
        
        bfs_queue = collections.deque()
        # Get All Island cells from this Start Point
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        visited = set()
        
        def dfs(r,c):

            grid[r][c]=2 
            bfs_queue.append((r,c,0))
            visited.add((r,c))

            for idx, idy in directions:
                nr = r + idx
                nc = c + idy
                if 0<=nr< n and 0 <=nc<n and grid[nr][nc]==1:
                    dfs(nr,nc)
                    
                    
            
        dfs(firstIsland_x,firstIsland_y)
       

        while bfs_queue:
            r, c, level = bfs_queue.popleft()
            if grid[r][c]==1: # Found Other Island
                return level - 1
            
            for idx, idy in directions:
                nr = r + idx
                nc = c + idy

                if 0<=nr< n and 0 <=nc<n and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    bfs_queue.append((nr, nc, level+1)) 
        return -1


        # [[1,1,1,1,1],
        # [1,0,0,0,1],
        # [1,0,1,0,1],
        # [1,0,0,0,1],
        # [1,1,1,1,1]]