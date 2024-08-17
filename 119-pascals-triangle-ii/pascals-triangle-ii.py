class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)
        # populate each row element

        #  This Below approcah works, cuz the row_index input is off by 1
        # 1-- -1
        # 11 --> 0
        # 121--> 1
        # 1331--> 2  range(rowIndx) doesnt include row index
        for i in range(1, rowIndex):
            # fill right before filling left
            #  you are going to add Left

            for j in range(i, 0, -1):
                # current element is sum of current and previous element in above row       
                
                row[j] += row[j - 1]
            # print(row)
        return row

        # Memoization
        # if rowIndex == 0:
        #     return [1]
        # if rowIndex == 1:
        #     return [1, 1]
        # prev_row = self.getRow(rowIndex-1)
        # new_row = [1 for _ in range(len(prev_row)+1)] #imp part
        
        # for i in range(1,len(prev_row)):
        #     new_row[i] = prev_row[i-1] + prev_row[i]
            
        # return new_row 

     

    