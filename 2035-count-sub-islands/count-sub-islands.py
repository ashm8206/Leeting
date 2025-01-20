class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # Brute:
        #  1. Find All Islands in grid 1 : (r,c)
        #. 2. Find All isalnds in grid 2: set : (r,c) keys
        #  3. For every island in 2 intesection 1 == len(2) ans+=1

        # How about this?
        # We count Number of SubIslands 
        # only from those cells that are both grid1==grid2==1

        # any island in grid2==1 that has grid1==0: 
        # has to be invalidated as it is not fully contained


        m = len(grid1)
        n = len(grid1[0])

        def dfs(i,j):
            if 0 <= i < m and  0 <= j < n and (i,j) not in visited and grid2[i][j]==1:
                visited.add((i,j))
                for nr, nc in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
                    dfs(nr,nc)

        def removeIsland(i,j):
            if 0 <= i < m and  0 <= j < n and grid2[i][j]==1:
                grid2[i][j] = 0 # unset/invalidate island

                for nr, nc in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
                    removeIsland(nr,nc)

        for i in range(m):
            for j in range(n):
                if grid2[i][j]==1 and grid1[i][j]==0:
                    removeIsland(i,j)
                    # we dont care about the reverse case
                    # grid1[1] and grid2[0]

        print(grid2)
        count = 0
        visited = set()
        for r in range(m):
            for c in range(n):
                if grid2[r][c]==1 and (r,c) not in visited:
                    dfs(r,c)
                    print(r,c)
                    count+=1
        return count
    


        