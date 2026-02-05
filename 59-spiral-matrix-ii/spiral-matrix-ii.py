class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0 for j in range(n)] for i in range(n)]

        up, left = 0, 0
        down, right = n-1, n-1

        val = 0
        row, col = 0, 0 
        # while i < n**2:

        while left<=right and up <= down:

            for col in range(left, right+1):
                result[up][col] = val+1
                val+=1
            up+=1

            for row in range(up, down+1):
                result[row][right] = val+1
                val+=1
            right-=1
         
            
            if up<=down:
                # rowStart <= rowEnd
                for col in range(right, left-1, -1):
                    result[down][col] = val+1
                    val+=1
                down-=1

            if left<=right:
                
                for row in range(down, up - 1, -1):
                    result[row][left] = val+1
                    val+=1
                left+=1
        return result
            