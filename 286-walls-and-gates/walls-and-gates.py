from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        m, n = len(rooms), len(rooms[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        INF = 2**31 - 1
        q = collections.deque()
        visited = set()

        for r in range(m):
            for c in range(n):
                if rooms[r][c]==0:
                    # gate idx and level, gates are at 0 level
                    q.append((r,c,0))
                    visited.add((r,c))

    
        while q:
            r, c, level = q.popleft()
            for x, y in directions:
                nr, nc = r+x, c+y
                if 0 <= nr < m and 0 <= nc < n and rooms[nr][nc]==INF and (nr,nc) not in visited:
                    rooms[nr][nc] = level+1
                    q.append((nr,nc,level+1))
                    visited.add((nr,nc))
        return rooms
                    


        

        