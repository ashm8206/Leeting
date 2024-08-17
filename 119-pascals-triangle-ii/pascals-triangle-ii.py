class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # row = [1]
        # for i in range(rowIndex):
        #     for j in range(i, 0, -1):
        #         row[j] = row[j] + row[j-1]
        #     row.append(1)
        # return row

        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        prev_row = self.getRow(rowIndex-1)
        new_row = [1 for _ in range(len(prev_row)+1)] #imp part
        
        for i in range(1,len(prev_row)):
            new_row[i] = prev_row[i-1] + prev_row[i]
            
        return new_row 

        # 3, 2,1,0

    