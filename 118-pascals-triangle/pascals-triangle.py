class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        if numRows >=2:
            res = [[1],[1,1]]
            prev = res[-1]
            for i in range(2, numRows):
                curr = [1]
                for j in range(1,i):
                    curr.append(prev[j] + prev[j-1])
                curr.append(1)
                res.append(curr)
                prev = curr
        return res 

        # res = [ [1 for j in range(i+1)] for i in range(numRows)]


        # # # Start i in range(2, numRows)
        # # # In col process [1, i]

        # for i in range(2, numRows):
        #     for j in range(1, i):
        #         res[i][j] = res[i-1][j-1] + res[i-1][j]
        # #         res[i][j] = res[i-1][j-1] + res[i-1][j] 

        # return res 
        