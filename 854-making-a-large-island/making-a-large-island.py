class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
    
        R,C = len(grid),len(grid[0])
        def get(i, j):
            return 0 if i < 0 or j < 0 or i >= R or j >= C else grid[i][j]


        def paint(i, j, color):
            if get(i, j) != 1: 
                return 0

            grid[i][j] = color
            return 1 + paint(i + 1, j, color) + paint(i - 1, j, color) + paint(i, j + 1, color) + paint(i, j - 1, color)




        sizes = [ 0, 0 ] # sentinel values; colors start from 2.
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1: 
                    sizes.append(paint(i, j, color=len(sizes)))

    
        res=0
        
        for i in range(R):
            for j in range(C):
                if not grid[i][j]:
                    # get the sizes of adjacent neighor
                    # print(i,j, sizes)
                    area = 0
                    seen = set()
                    for r, c in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                        if 0 <=r<R and 0<=c<C:
                            color = grid[r][c]
                            
                            if color not in seen:
                                # print(color, sizes[color])
                                area += sizes[color] 
                                seen.add(color)
                            # sum all four, if there was an island it will increase      
                    # print(area)
                    res = max(res, 1 + area)

                    
                    # res = max(res, 1 + sum(sizes[c] for c in {get(i + 1, j), get(i - 1, j), get(i, j + 1), get(i, j - 1)}))
        return R*C if not res else res









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
        