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

        for r1 in range(r):
            for r2 in range(r1, r):

                hmap = {0:1} # 1 time we have seen prefix [0]

                for col in range(c):
                    # print((r2,col),(r1-1,col))
                    curr_sum = ps[r2+1][col+1] - (ps[r1][col+1] if r1 > 0 else 0)
                    diff = curr_sum - target

                    res+= hmap.get(diff, 0)

                    hmap[curr_sum] = hmap.get(curr_sum, 0) + 1
        return res

        # Method II
        # R = len(matrix)
        # C = len(matrix[0])
        # answer = 0
        # for r1 in range(R):
        #     sums = [0] * C
           
        #     for r2 in range(r1, R):
        #         sumFreq = {0: 1}
        #         rowSum =  0
                
        #         for c in range(C):
        #             # print(rowSum, sums[c])
        #             rowSum += matrix[r2][c]
        #             sums[c] += rowSum
        #             # sums[c]+= matrix[r2][c]

        #             answer += sumFreq.get(sums[c] - target, 0)
        #             sumFreq[sums[c]] = sumFreq.get(sums[c], 0) + 1
        #             # print("****", (r2,c))
        # return answer
