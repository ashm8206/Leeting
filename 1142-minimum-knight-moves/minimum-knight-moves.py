from collections import deque
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:


        q = deque([(0, 0, 0)])
        visited = set({(0,0)})

        while q:
            r, c, dest = q.popleft()
            if (r, c) == (x,y):
                return dest

            directions = [(r+2,c+1), (r+2,c-1),(r-2,c+1), (r-2,c-1), (r-1,c-2), (r+1,c-2), (r-1,c+2), (r+1,c+2)]

            for nr, nc in directions:
            # if 0 <= nr < n and 0 <= nc < n:
                if (nr,nc) not in visited:
                    q.append((nr,nc, dest+1))
                    visited.add((nr, nc))
        return -1

        