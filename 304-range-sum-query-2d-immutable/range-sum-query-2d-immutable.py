class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        ROWS, COLS = len(matrix), len(matrix[0])
        
        

        self.prefix_mat = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        
        for r in range(ROWS):
            for c in range(COLS):
                above = 0 if r == 0 else self.prefix_mat[r-1][c]
                left =  0 if c == 0 else self.prefix_mat[r][c-1]
                topRight = 0 if (c==0 or r==0) else self.prefix_mat[r-1][c-1]       
                
                self.prefix_mat[r][c] = above + left - topRight + matrix[r][c]
              
        # self.prefix_mat = [[0]*(COLS+1) for _ in range(ROWS+1)]
        
        # for r  in range(ROWS):
        #     for c in range(COLS):
        #         self.prefix_mat[r+1][c+1] = self.prefix_mat[r][c+1] + self.prefix_mat[r+1][c] - self.prefix_mat[r][c] + matrix[r][c]
        
        # print(self.prefix_mat)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1, col1, row2, col2

        bottomRight = self.prefix_mat[row2][col2]
        above = self.prefix_mat[row1-1][col2] if row1 > 0 else 0
        left = self.prefix_mat[row2][col1-1] if col1 > 0 else 0
        topRight = self.prefix_mat[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0

        return bottomRight - above -left + topRight


            

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)