from collections import deque
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])


        #WHY LEFT AND UP?
        """Since we are traversing the grid from left to right, and from top to bottom, for each land cell we are currently at, we only need to check whether the LEFT and UP cells are land cells with a slight modification on previous approach."""



        result = 0 #up and left
      
        for r in range(m):
            for c in range(n):
                if grid[r][c]==1:
                    result+=4

                    if r > 0 and grid[r-1][c] ==1:
                        result -=2 #1 from each land mass boundary

                    if c > 0 and grid[r][c-1] ==1:
                        result -=2 #1 from each land mass
        return result


           

        