class NumMatrix:

    def create_prefix_sum(self,row):
        n = len(row)
        prefix_sum = [0]*(n)
       
        for i in range(n):
            if i > 0:
                prefix_sum[i] = prefix_sum[i-1] + row[i]
            else:
                prefix_sum[i] =  row[i]
        return prefix_sum
        
    def __init__(self, matrix: List[List[int]]):
        #create this 
        self.matrix = matrix
        self.row_prefix_sum = []
        for row in matrix:
            prefix_sum = self.create_prefix_sum(row)
            self.row_prefix_sum.append(prefix_sum)
        

    def update(self, row: int, col: int, val: int) -> None:

        self.matrix[row][col]=val
        self.row_prefix_sum[row] = self.create_prefix_sum(self.matrix[row])
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # iterate throught row1 to row2
        region_sum = 0 
        for r in range(row1, row2+1):

            if col1==0:
                region_sum += self.row_prefix_sum[r][col2]
            else:
                region_sum += self.row_prefix_sum[r][col2] - self.row_prefix_sum[r][col1-1]
        
        return region_sum
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)