class NumMatrix:

    # https://www.youtube.com/watch?v=KE8MQuwE2yA

    # def __init__(self, matrix: List[List[int]]):
    #     self.prefix_mat = [[0]*len(matrix[0]) for _ in range(len(matrix))]

    #     for r in range(len(matrix)):
    #         for c in range(len(matrix[0])):
    #             if c == 0:
    #                 self.prefix_mat[r][c] = matrix[r][c]
    #             else:
    #                 self.prefix_mat[r][c] = self.prefix_mat[r][c-1] + matrix[r][c]
        
    #     # print(self.prefix_mat)

    # def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
  
    #     result = 0
    #     for r in range(row1, row2 + 1):
    #         if col1 > 0:
    #             result += self.prefix_mat[r][col2] - self.prefix_mat[r][col1-1]
    #         else:
    #             result+= self.prefix_mat[r][col2] 
    #     return result

    def __init__(self, matrix: List[List[int]]):

        ROWS, COLS = len(matrix), len(matrix[0])

        self.prefix_mat = [[0]*(COLS+1) for _ in range(ROWS+1)]
        
        for r  in range(ROWS):
            for c in range(COLS):
                self.prefix_mat[r+1][c+1] = self.prefix_mat[r][c+1] + self.prefix_mat[r+1][c] - self.prefix_mat[r][c] + matrix[r][c]
        
        # print(self.prefix_mat)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1

        bottomRight = self.prefix_mat[row2][col2]
        above = self.prefix_mat[row1-1][col2]
        left = self.prefix_mat[row2][col1-1]
        topRight = self.prefix_mat[row1-1][col1-1]

        return bottomRight - above -left + topRight


            

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)