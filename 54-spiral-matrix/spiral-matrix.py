class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])

        left = 0
        right = m - 1
        top = 0
        down = n-1
        result = []

        while left <= right and top <= down:
            for j in range(left, right+1):
                result.append(matrix[top][j])
            top+=1
            
            for i in range(top, down+1):
                result.append(matrix[i][right])
            right-=1

            # not the same row
            
            if top<=down:
                for j in range(right, left-1, -1):
                    result.append(matrix[down][j])
                down-=1

            # not the same column
            if left<=right:
                for i in range(down, top - 1, -1):
                    result.append(matrix[i][left])
                left+=1
            
            # print(result, top, down, left, right)
        return result
            
            







        result = []
        rows, columns = len(matrix), len(matrix[0])
        up = left = 0
        right = columns - 1
        down = rows - 1

        while len(result) < rows * columns:
            # Traverse from left to right.
            # print(left,"L--R>", right)
            # print(up+1,"U--D>", down)
            # print(right-1,"R--L>", left)
            # print(down-1,"D--U>", up+1)
            # print("****")
            for col in range(left, right + 1):
                result.append(matrix[up][col])
            # Traverse downwards.
            for row in range(up + 1, down + 1):
                result.append(matrix[row][right])

            # Make sure we are now on a different row.
            if up != down:
            # Traverse from right to left.
                for col in range(right - 1, left - 1, -1):
                    result.append(matrix[down][col])

            # Make sure we are now on a different column.
            if left != right:
                # Traverse upwards.
                for row in range(down - 1, up, -1):
                    result.append(matrix[row][left])
            up += 1
            left += 1

            right -= 1
            down -= 1

        return result


            