class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)
        n = len(grid[0])
        

        def dfs(i,j):
           
            if i < 0 or i >= m or  j < 0 or j >= n or grid[i][j]!="1" or (i,j) in seen:
                return 
            # watch out

            # watch out for seen
            
            seen.add((i,j))
            for nr, nc in [(i-1,j),(i+1,j), (i,j+1), (i,j-1)]:
                # if 0 <= nr < m and 0<=nc < n and grid[nr][nc]=="1" and (nr,nc) not in seen:
                # watch out

                    dfs(nr,nc)
                    
                    
        seen = set()
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1" and (i,j) not in seen:
                    dfs(i,j)
                    count+=1
           
        return count











        
        # M = len(grid)
        # N = len(grid[0])
        # seen = set()

        
        # def dfs(i,j):

        #     if i < 0 or i >=M or j < 0 or j >=N or (i,j) in seen:
        #         return
            
        #     if grid[i][j]== "1":
        #         seen.add((i,j))
        #         dfs(i+1,j)
        #         dfs(i-1,j)
        #         dfs(i,j-1)
        #         dfs(i,j+1)
        #     return 
        

        # count = 0
        # for i in range(M):
        #     for j in range(N):
        #         if grid[i][j]== "1" and (i,j) not in seen:
        #             dfs(i,j)
        #             count+=1
        # return count