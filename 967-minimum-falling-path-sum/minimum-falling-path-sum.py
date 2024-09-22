from collections import defaultdict, deque
class Solution:
    
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        # BFS
        # m = len(matrix)
        # n = len(matrix[0])

        # minFal = float("inf")
        # queue = deque()
        # hmap = defaultdict(lambda : 10**5)
        # for j in range(n):
        #     queue.append((0,j))
        #     hmap[(0,j)] = matrix[0][j]
       

        # while queue:
        #     r, c = queue.popleft()
        #     sumSoFar = hmap[(r,c)]
            
        
        #     for dx, dy in [(1,-1), (1,0),(1,1)]:
        #         nr, nc = r + dx, c + dy

        #         if 0<=nr < m and 0 <= nc < n:
                  
        #             if matrix[nr][nc] + sumSoFar <= hmap[(nr,nc)]:

        #                 hmap[(nr, nc)] = matrix[nr][nc] + sumSoFar
        #                 queue.append((nr,nc))

        
        # for j in range(n):
            
        #     minFal = min(minFal, hmap[(m-1,j)])
        # return minFal 

        
        minFal = float("inf")
        m = len(matrix)
        n = len(matrix[0])

        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    matrix[i][j] += min( matrix[i-1][j],  matrix[i-1][j+1])
                
                elif j==n-1:
                    matrix[i][j] += min( matrix[i-1][j-1],  matrix[i-1][j])
                
                else:
                    matrix[i][j] += min( matrix[i-1][j-1],  min(matrix[i-1][j],(matrix[i-1][j+1])))
        
        for j in range(n):
            minFal = min(minFal, matrix[m-1][j])
        return minFal