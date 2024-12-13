class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        # 1 and 0  but "/" [0][n-1] ...[1][n-2] ..[n-1][0]

        n = len(grid)
        grid_expanded = [[0 for j in range(n*3)] for i in range(n*3)]

        for i in range(n):
            for j in range(n):
                base_i = i * 3
                base_j = j * 3

                if grid[i][j]=="/":
                    grid_expanded[base_i][base_j+2]= 1
                    grid_expanded[base_i+1][base_j+1]= 1
                    grid_expanded[base_i+2][base_j]= 1

                elif grid[i][j]=="\\":
                    grid_expanded[base_i][base_j]= 1
                    grid_expanded[base_i+1][base_j+1]= 1
                    grid_expanded[base_i+2][base_j+2]= 1

                
        
        visited = set()

        def dfs(r,c):

            if r< 0 or r >= n*3 or c<0 or c >= n*3 or (r,c) in visited:
                return
            
            if grid_expanded[r][c]==0:
                visited.add((r,c))
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c-1)
                dfs(r, c+1)
        
     
        regions = 0
        for i in range(n*3):
            for j in range(n*3):
                if grid_expanded[i][j]==0 and (i,j) not in visited:
                    dfs(i,j)
                    regions+=1
        return regions
