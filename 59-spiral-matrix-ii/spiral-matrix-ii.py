class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0 for j in range(n)] for i in range(n)]

        up, left = 0, 0
        down, right = n-1, n-1

        i = 0
        row, col = 0, 0 
        while i < n**2:

            for col in range(left, right+1):
                result[row][col] = i+1
                i+=1
        

            for row in range(up+1, down+1):
                result[row][col] = i+1
                i+=1
         
            
            if up!=down:
                # if row is diff, then it makes 
                # sense to go L-->R and R-->L
                for col in range(right-1, left-1, -1):
                    result[row][col] = i+1
                    i+=1
            

            if left!=right:
                for row in range(down-1, up, -1):
                    result[row][col] = i+1
                    i+=1
             
            left +=1
            up+=1
            down-=1
            right-=1

        return result
            