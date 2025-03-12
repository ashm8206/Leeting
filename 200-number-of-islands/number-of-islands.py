class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count =  0
        n = len(grid)
        m = len(grid[0])
        seen = set()

        def dfs(r, c):

            seen.add((r,c))
            for dx, dy in [[0,1],[1,0],[0,-1], [-1,0]]:
                nr = r + dx
                nc = c + dy
                if 0 <= nr < n and 0 <= nc< m and (nr,nc) not in seen and grid[nr][nc]=="1":
                    dfs(nr,nc)


        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1" and (i,j) not in seen:
                    dfs(i,j)
                    count+=1
        return count