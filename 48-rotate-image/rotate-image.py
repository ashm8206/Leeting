class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 1 4 7
        # 2,5 8
        # 3 6 9
        self.transposeReflect(matrix)
        # self.reflect(matrix)
    def transposeReflect(self, matrix):
        n = len(matrix)
        # works only cuz its N*N
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] =  matrix[j][i], matrix[i][j]
            
            # matrix[i]= matrix[i][::-1]
            # Half Time
            for k in range(n//2):
                matrix[i][k], matrix[i][n-1-k]  = matrix[i][n-1-k], matrix[i][k]
        


                    
    # def reflect(self, matrix):
    #         n = len(matrix)
            # for i in range(n):
            #     for j in range(n//2):
            #         matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]

    # 1, 2.     3, 1
    # 3, 4.     4 2
    
    # Test is  target is a rotation of src
    # for i in range(n):
    #     for j in range(i, n):
    #             if mat[i][j] == mat[j][n-i-1]:
                    
    #                 continue:
    #             else:
    #                 return False
    #     return True
