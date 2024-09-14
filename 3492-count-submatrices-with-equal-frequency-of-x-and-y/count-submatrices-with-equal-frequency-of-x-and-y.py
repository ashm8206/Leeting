class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        
        # n = len(grid)
        # m = len(grid[0])

        # prefix = [ [{'X':0, 'Y':0} for j in range(m) ]for i in range(n)]
        
        # # Count Prefix
        # for i in range(n):
        #     for j in range(m):
        #         prefix[i][j]['X'] = 1 if grid[i][j] == 'X' else 0
        #         prefix[i][j]['Y'] = 1 if grid[i][j] == 'Y' else 0
        #         if i > 0:
                    
        #             prefix[i][j]['X'] += prefix[i-1][j]['X']
        #             prefix[i][j]['Y'] += prefix[i-1][j]['Y']
        #         if j > 0:
                    
        #             prefix[i][j]['X'] += prefix[i][j-1]['X']
        #             prefix[i][j]['Y'] += prefix[i][j-1]['Y']

        #         if i > 0 and j > 0:
                    
        #             prefix[i][j]['X'] -= prefix[i-1][j-1]['X']
        #             prefix[i][j]['Y'] -= prefix[i-1][j-1]['Y']
        # # print(prefix)          
        # cnt = 0
        # for i in range(n):
        #     for j in range(m):
        #         if prefix[i][j]['X'] > 0 and prefix[i][j]['X'] == prefix[i][j]['Y']:            
                    
        #             cnt+=1
        # return cnt

        # on the fly

        m, n = len(grid), len(grid[0])
        X = [[0] * (n + 1) for i in range(m + 1)]
        Y = [[0] * (n + 1) for i in range(m + 1)]
        res = 0
        for i in range(m):
            for j in range(n):
                X[i][j] = X[i-1][j] + X[i][j-1] - X[i-1][j-1] + (grid[i][j] == "X")
                Y[i][j] = Y[i-1][j] + Y[i][j-1] - Y[i-1][j-1] + (grid[i][j] == "Y")
                if X[i][j] == Y[i][j] > 0: res += 1
        return res