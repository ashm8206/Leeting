class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        mod = 10**9 + 7

        dp = [[-1] * n for _ in range(m)]

        directions = [(-1,0),(1,0), (0,1), (0,-1)]

        def dfs(i,j, prev):
            
            if dp[i][j]!=-1:
                return dp[i][j]
            
            res = 1
            for dx, dy in directions:
                nx, ny = i + dx, j + dy
                if 0 <= nx < m and  0 <= ny < n and grid[nx][ny] > prev:
                    res = (res +  dfs(nx, ny, grid[nx][ny]))% mod
            dp[i][j] = res 
            return dp[i][j]

        ans = 0
        for i in range(m):
            for j in range(n):
                ans= (ans + dfs(i, j, grid[i][j])) % mod
        return ans 