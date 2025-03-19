class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:


        N = len(grid)
        M = len(grid[0])
        seen = set()

        def get_area(r,c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                    and (r, c) not in seen and grid[r][c]==1):
                return 0

            seen.add((r, c))

            ans = 1 # Imp
            ans+=get_area(r+1, c)
            ans+=get_area(r-1, c)
            ans+=get_area(r, c-1) 
            ans+= get_area(r, c+1)
            return ans

            # return (1 + get_area(r+1, c) + get_area(r-1, c) +
            #         get_area(r, c-1) + get_area(r, c+1))


        max_area = 0
        for r in range(N):
            for c in range(M):
                if grid[r][c]==1 and (r,c) not in seen:
                    max_area = max(max_area,get_area(r,c))
        return max_area
