class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix_mat = [[0]*len(matrix[0]) for _ in range(len(matrix))]

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if c == 0:
                    self.prefix_mat[r][c] = matrix[r][c]
                else:
                    self.prefix_mat[r][c] = self.prefix_mat[r][c-1] + matrix[r][c]
        
        # print(self.prefix_mat)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
  
        result = 0
        for r in range(row1, row2 + 1):
            if col1 > 0:
                result += self.prefix_mat[r][col2] - self.prefix_mat[r][col1-1]
            else:
                result+= self.prefix_mat[r][col2] 
        return result


            

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)