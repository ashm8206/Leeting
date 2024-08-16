class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        # Row nlog M = M*N 
        # top = 0
        # bottom = len(mat)-1
        # while bottom > top:
        #     mid = (top + bottom) // 2
        #     if max(mat[mid]) > max(mat[mid+1]):
        #         bottom = mid
        #     else:
        #         top = mid+1
        # return [bottom,mat[bottom].index(max(mat[bottom]))]

        # rows, cols = len(mat), len(mat[0])
        # leftCol, rightCol = 0, cols
        # while leftCol < rightCol:
        #     col = leftCol + (rightCol - leftCol) // 2
        #     row = max(range(rows), key=lambda r: mat[r][col])
        #     left = mat[row][col-1] if col > 0 else -1
        #     right = mat[row][col+1] if col < cols - 1 else -1
        #     if mat[row][col] > left and mat[row][col] > right:
        #         return (row, col)
        #     elif mat[row][col] < left:
        #         rightCol = col
        #     else:
        #         leftCol = col + 1
        # return []

        l, r = 0, len(mat) - 1
        while l < r:
            i = (l + r) // 2
            j = mat[i].index(max(mat[i]))

            down = mat[i+1][j] if i+1 < len(mat) else -1

            if mat[i][j] < down:
                l = i + 1
            else:
                r = i
        
        return [l, mat[l].index(max(mat[l]))]