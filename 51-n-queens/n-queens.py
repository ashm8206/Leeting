class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        results = []
        
        def constraintValid(slate):
            last= len(slate)
            if last < 2:
                return True
            else:
                for i in range(last-1):
                    rowdiff = abs(last-1-i)
                    coldiff = abs(slate[last-1]-slate[i])
                    if slate[i]==slate[last-1] or rowdiff==coldiff:
                        return False
                return True

        def helper(row, slate, diag, anti_diag):
          
            if row==n:
                results.append(["."*col+"Q"+"."*(n-1-col) for col in slate])
                return
            
            for col in range(n):
                if col not in slate and row+col not in diag and row-col not in anti_diag:
                    slate.append(col)
                    diag.append(row+col)
                    anti_diag.append(row-col)

                    helper(row+1,slate, diag, anti_diag)
                    
                    slate.pop()
                    diag.pop()
                    anti_diag.pop()
            
        
        helper(0,[],[],[])
        return results