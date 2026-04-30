class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        # rows = [set() for _ in range(N)]
        # cols = [set() for _ in range(N)]
        # box = [set() for _ in range(N)]

        row = [000000000 for _ in range(N)]
        col = [000000000 for _ in range(N)]
        box = [000000000 for _ in range(N)]

        for r in range(N):
            for c in range(N):
                val = board[r][c]
                if  val =='.':
                    continue
                val = int(val)

                # 9 bit integer represents 9 bit of sudoku board

                if row[r] & (1 << val): # check if ith bit is set?
                    return False
                row[r] = row[r] | (1 << val) # if not set, then set it

                # if val in rows[r]:
                #     return False
                # rows[r].add(val)

                if col[c] & (1 << val):
                    return False
                col[c] = col[c] | (1 << val)

                # if val in cols[c]:
                #     return False
                # cols[c].add(val)

                boxIndex= (r//3)*3 + (c//3)
                # box_row * total_cols + box_col

                if box[boxIndex] & (1 << val):
                    return False
                box[boxIndex] = box[boxIndex] | (1 << val)

                # if val in box[boxIndex]:
                #     return False
                # box[boxIndex].add(val)
        return True

    # 0 --> 111111111
    # 1 --> Check (x & (1 << i))
    # 8 --> Set (x | (1 << i))
                


