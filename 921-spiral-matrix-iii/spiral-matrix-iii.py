class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
     
        directions =  [[0, 1], [1, 0], [0, -1], [-1, 0]] # east, south, west, north
        res= [[rStart, cStart]] 
        length = 0
        d = 0
        while(len(res) < rows*cols):

            if d==0 or d == 2:
                length+=1
            
            for _ in range(length):
                rStart += directions[d][0]
                cStart += directions[d][1]

                if rStart >= 0 and rStart < rows and cStart >= 0 and cStart < cols: # check valid
                    res.append([rStart, cStart])
            
            d = (d+1)%4
        return res