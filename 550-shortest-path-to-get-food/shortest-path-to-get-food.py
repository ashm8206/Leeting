class Solution:
    def getFood(self, grid: List[List[str]]) -> int:

        m, n = len(grid), len(grid[0])
        seen = set()
        q = collections.deque()

        for i in range(m):
            for j in range(n):
                # if grid[i][j]=='*':
                #     q.append((i,j,0))
                if grid[i][j]=="#":
                    q.append((i,j,0))

        while q:
            r, c, d = q.popleft()
            seen.add((r,c))
            if grid[r][c]=="*":
                return d

            for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                nr = r + dx
                nc = c + dy
                if 0 <=nr<m and 0<=nc<n:
                    if grid[nr][nc]!='X' and (nr,nc) not in seen:
                        # if grid[nr][nc]=='#':
                        #     return d+1
                        seen.add((nr,nc))
                        q.append((nr,nc,d+1))
        return -1