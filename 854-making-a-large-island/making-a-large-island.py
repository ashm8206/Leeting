class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        # 1. Get area in list where i = color starting at 2
        # components = [0...N] 
        # i = color and components[i] = size of area

        # 2. for every r,c grid[r][c] == 0
        #    1. get colors of neigbors in  a set 
        #    2. Add the sizes of distinct color to area

        # 3. maxmize res:
        #    res  = max(res, 1+area)
    
       
        if not grid or not grid[0]:
            return 0
    
        rows, cols = len(grid), len(grid[0])
        
        # DFS to paint each connected component with a unique color
        def paint(i, j, color):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] != 1:
                return 0
                
            grid[i][j] = color
            # Explore in all four directions
            return 1 + paint(i+1, j, color) + paint(i-1, j, color) + \
                    paint(i, j+1, color) + paint(i, j-1, color)
        
        # Paint each island with a unique color (starting from 2)
        # and record its size
        island_sizes = [0, 0]  # Colors start from 2
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    island_sizes.append(paint(i, j, len(island_sizes)))
        
        # Find the best place to fill with 1
        max_size = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    # Get unique adjacent colors and sum their sizes
                    neighbors = set()
                    for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                        if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] > 1:
                            neighbors.add(grid[ni][nj])
                    
                    # New island size = 1 (the cell itself) + sum of connected islands
                    size = 1 + sum(island_sizes[color] for color in neighbors)
                    max_size = max(max_size, size)
        
        # If grid is all 1s already, return total size
        return rows * cols if max_size == 0 else max_size








        # g = grid
        # R,C=len(g),len(g[0])
        # def get(i, j):
        #     return 0 if i < 0 or j < 0 or i >= R or j >= C else g[i][j]
        # def paint(i, j, clr):
        #     if get(i, j) != 1: return 0
        #     g[i][j] = clr
        #     return 1 + paint(i + 1, j, clr) + paint(i - 1, j, clr) + paint(i, j + 1, clr) + paint(i, j - 1, clr)
        # sizes = [ 0, 0 ] # sentinel values; colors start from 2.
        # for i in range(R):
        #     for j in range(C):
        #         if g[i][j] == 1: sizes.append(paint(i, j, len(sizes)))
        # res=0
        # for i in range(R):
        #     for j in range(C):
        #         if not g[i][j]:
        #             # need to use set to remove duplicate as there could be some valid flip position 
        #             # which is closed to the same area multiple times. 
        #             res = max(res, 1 + sum(sizes[c] for c in {get(i + 1, j), get(i - 1, j), get(i, j + 1), get(i, j - 1)}))
        # return R*C if not res else res
        