class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        # https://leetcode.com/problems/range-sum-query-2d-immutable/editorial/

        r, c = len(matrix), len(matrix[0])
        
        # compute 2D prefix sum
        ps = [[0] * (c + 1) for _ in range(r + 1)]
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                ps[i][j] = ps[i - 1][j] + ps[i][j - 1] - ps[i - 1][j - 1] + matrix[i - 1][j - 1]


        res = 0

        for r1 in range(1, r+1):
            for r2 in range(r1, r+1):

                hmap = {0:1} # 1 time we have seen prefix [0]

                for col in range(1, c+1):

                    curr_sum = ps[r2][col] - ps[r1 - 1][col]
                    diff = curr_sum - target

                    res+= hmap.get(diff, 0)

                    hmap[curr_sum] = hmap.get(curr_sum, 0) + 1
        return res
