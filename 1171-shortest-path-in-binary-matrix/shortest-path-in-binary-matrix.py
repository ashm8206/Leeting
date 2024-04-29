class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        seen = set()
        q = collections.deque()

        n = len(grid) - 1
        # N*N matrix

        if grid[0][0] != 0 or grid[n][n] != 0:
            return -1
        
        #Single Source
        q.append((0,0,1))
        seen.add((0,0))
        
        while q:
            r, c, d = q.popleft()

            if r==n and c == n:
                return d
            for dx, dy in [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)]:
                nr = r + dx
                nc = c + dy
                # print(nr,nc)
                if 0 <= nr <= n and 0 <= nc <= n:
                    if grid[nr][nc]==0 and (nr,nc) not in seen:
                        
                        seen.add((nr,nc))
                        q.append((nr,nc,d+1))
        return -1

        [[0,1],
         [1,0]]