from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
       
 
        ROWS = len(mat)
        COLS = len(mat[0])
        matrix = mat
        # q = deque()
        # visited = set()
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if matrix[r][c]==0:
        #             q.append((r,c,0))
        #             visited.add((r,c))
                    
        # dirs = [(0,1),(1,0),(0,-1),(-1,0)];
        # while q:
        #     r, c, steps = q.popleft()
        #     for dx, dy in dirs:
        #         nr = r+dx
        #         nc = c+dy
        #         if ROWS >nr>=0 and COLS>nc>=0 and (nr,nc) not in visited:
        #             visited.add((nr,nc))
                    
        #             matrix[nr][nc] = steps + 1
        #             q.append((nr,nc, steps+1))
        # return matrix


        # If you start BFS from 1 
        # It gives you shortest Path from 1
        
        # We need to find the distance of the nearest 0


        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] != 0:
                    top, left = inf, inf
                    if i-1 >=  0:
                        top = matrix[i-1][j]

                    if j-1 >= 0:
                        left = matrix[i][j-1]

                    matrix[i][j] = min(top,left) + 1

            
        for i in range(ROWS-1, -1, -1):
            for j in range(COLS-1, -1, -1):
                if matrix[i][j] !=0:
                    bottom, right = inf, inf
                    if  i+1 < ROWS :
                        bottom = matrix[i+1][j]

                    if j+1 < COLS:
                        right = matrix[i][j+1]

                    matrix[i][j] = min(matrix[i][j],min(bottom,right)+ 1)

        return matrix