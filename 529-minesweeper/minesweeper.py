class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1), (1, -1), (-1, 1),(1, 1), (-1, -1)]
        
        m, n = len(board), len(board[0])
        def dfs(board,i,j):
            if i < 0 or i >=m or j < 0 or j >=n:
               return
            
            if board[i][j]=='M':
                board[i][j] = 'X'
                
            
            elif board[i][j]=='E':
                mine = sum( board[i+x][j+y] == 'M' for x, y in directions if 0 <= i+x < m and  0<=j+y < n)

                if mine > 0:
                    board[i][j] = str(mine)
                    
                else:
                    board[i][j]='B'

                    for x, y in directions:
                        dfs(board, i+x, j+y)
            return board


        
        return dfs(board,*click)
