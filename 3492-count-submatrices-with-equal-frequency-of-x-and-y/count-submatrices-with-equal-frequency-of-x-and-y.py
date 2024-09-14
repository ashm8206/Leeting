class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        
        n = len(grid)
        m = len(grid[0])

        prefix = [ [{'X':0, 'Y':0} for j in range(m) ]for i in range(n)]
        
        # Count Prefix
        for i in range(n):
            for j in range(m):
                prefix[i][j]['X'] = 1 if grid[i][j] == 'X' else 0
                prefix[i][j]['Y'] = 1 if grid[i][j] == 'Y' else 0
                if i > 0:
                    
                    prefix[i][j]['X'] += prefix[i-1][j]['X']
                    prefix[i][j]['Y'] += prefix[i-1][j]['Y']
                if j > 0:
                    
                    prefix[i][j]['X'] += prefix[i][j-1]['X']
                    prefix[i][j]['Y'] += prefix[i][j-1]['Y']

                if i > 0 and j > 0:
                    
                    prefix[i][j]['X'] -= prefix[i-1][j-1]['X']
                    prefix[i][j]['Y'] -= prefix[i-1][j-1]['Y']
        # print(prefix)          
        cnt = 0
        for i in range(n):
            for j in range(m):
                if prefix[i][j]['X'] > 0 and prefix[i][j]['X'] == prefix[i][j]['Y']:            
                    
                    cnt+=1
        return cnt