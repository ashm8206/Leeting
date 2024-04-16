class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        n = len(mat)

        def rotate(mat):

            res = [[0]*n for _ in range(n)]
            

            for i in range(n):
                for j in range(n):
                    res[j][i] = mat[i][j]
            
            for i in range(n):
                res[i] = res[i][::-1]   
            return res


        def match(src,target):

            for i in range(n):
                for j in range(n):
                    if mat[i][j]!=target[i][j]:
                        return False
            return True
        
        count = 4 # 0 --> 4 is equal
        for i in range(count): #0, 1, 2
            mat = rotate(mat)
            if match(mat, target):
                return True
            
        return False



        