from collections import deque
class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()

        N = len(grid)
        M = len(grid[0])
        count = 0

        # DFS : O(M * N), O min(M,N)
        # def dfs(i,j):

        #     if i<0 or i>=N or j<0 or j>=M or (i,j) in seen:
        #         return

        #     if grid[i][j]=="1":
        #         seen.add((i,j))
        #         dfs(i-1,j)
        #         dfs(i+1,j)
        #         dfs(i,j-1)
        #         dfs(i,j+1)

        queue = deque()
        def bfs(r,c):
        
            while queue:
                r, c = queue.popleft()

                for nr, nc in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
                    if 0<= nr < N and 0 <= nc < M and grid[nr][nc] == '1' and (nr,nc) not in seen:
                        queue.append((nr,nc))
                        seen.add((nr,nc))



        for i in range(N):
            for j in range(M):
                if grid[i][j]=="1" and (i,j) not in seen:
                    # dfs(i,j)
                    seen.add((i,j))
                    queue.append((i,j))
                    bfs(i,j)
                    count += 1
        return count


        # BFS : O(M * N), O min(M,N)

        # def bfs():

        #     queue = deque()
        #     for i in range(n):
        #         for j in range(m):
        #             if grid[i][j]=="1" and (i,j) not in seen:
        #                 nonlocal count
        #                 count += 1
        #                 queue.append(i*m + j)
        #                 seen.add((i,j))
        #             while queue:
        #                 idx = queue.popleft()
        #                 row = idx // m
        #                 col = idx % m

        #                 if row-1 >=0 and grid[row-1][col]=='1' and (row-1,col) not in seen:
        #                     queue.append((row-1)*m + col)
        #                     seen.add((row-1,col))

        #                 if col-1 >=0 and grid[row][col-1]=='1' and (row,col-1) not in seen:
        #                     queue.append(row*m + (col - 1))
        #                     seen.add((row,col-1))
        #                 if row+1 < n and grid[row+1][col]=='1' and (row+1,col) not in seen:
        #                     queue.append((row+1)*m + col)
        #                     seen.add((row+1,col))

        #                 if col+1 < m and grid[row][col+1]=='1' and (row,col+1) not in seen :
        #                     queue.append(row*m + (col +1))
        #                     seen.add((row,col+1))
        #     return count
        
        # return bfs()
                    

        