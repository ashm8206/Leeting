class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 or numRows >= len(s):
            return s
        
        lists = [[] for _ in range(numRows)]
        row_idx = 0
        direction = 1
        
        for char in s:
            lists[row_idx].append(char)

            
            if row_idx == numRows - 1:
                direction = -1
            elif row_idx == 0:
                direction = 1

            row_idx += direction
        
        # print(lists)
        return "".join(["".join(row) for row in lists])
        # result = "".join("".join(row) for row in lists)
        # return result

        # if numRows == 1:
        #     return s

        # increment = 2*(numRows-1)
        # # go numRow-1 steps down and again Go Up
        # # Neetcode https://www.youtube.com/watch?v=Q2Tw6gcVEwc
        # ans = [""]*numRows

        # n = len(s)

        # for curr_row in range(numRows):
            
        #     for i in range(curr_row, len(s), increment):
        #         ans[curr_row]+=s[i]

        #         if curr_row > 0 and curr_row < numRows-1:
        #             # If its in Middle Row
        #             # i+increment ( increment/section steps from Curr index - 2*currRow)
        #             # -  2*curr_row every time
        #             if (i+increment-2*curr_row) < len(s):
        #                 ans[curr_row] += s[i+increment-2*curr_row]
        

        # return "".join(ans)

        # P0    A4    H8     N12
        # A1 P3 L5 S7 I9 I11 G13
        # Y2    I6    R10

    
        # P0     I6    N
        # A1   L5 S7  I G
        # Y2 A4   H8 R
        # P3      I9

        # Skip =  nrows + (nrows-2) = 
        # odd + (odd-even) = odd + odd = even
        # even + (even-even) = even + even = even
