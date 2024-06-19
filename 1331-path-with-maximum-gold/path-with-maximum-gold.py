class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        

        def backtrack(r,c):

            if r < 0 or c < 0 or r >= R or c >= C or grid[r][c] == 0:
                return 0
            
            max_gold = 0

            visited.add((r,c))

            for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr = r + dx
                nc = c + dy
                if (nr,nc) not in visited:
                    max_gold = max(max_gold, backtrack(nr,nc))
            
            visited.remove((r,c))

            # find the max from each of the paths and add that to parent

            return max_gold + grid[r][c]
        

        
        R = len(grid)
        C = len(grid[0])

        visited = set()
        maxGold = 0

        for r in range(R):
            for c in range(C):
                if grid[r][c]!=0:
                        gold = backtrack(r,c)
                        # you need to maximoze the starting point
                        maxGold = max(maxGold, gold)

        return maxGold