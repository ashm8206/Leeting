from collections import deque
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:


        # q = deque([(0, 0, 0)])
        # visited = set({(0,0)})

        # while q:
        #     r, c, dest = q.popleft()
        #     if (r, c) == (x,y):
        #         return dest

        #     directions = [(r+2,c+1), (r+2,c-1),(r-2,c+1), (r-2,c-1), (r-1,c-2), (r+1,c-2), (r-1,c+2), (r+1,c+2)]

        #     for nr, nc in directions:
        #     # if 0 <= nr < n and 0 <= nc < n:
        #         if (nr,nc) not in visited:
        #             q.append((nr,nc, dest+1))
        #             visited.add((nr, nc))
        # return -1

        offsets = [(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]

        origin_queue = deque([(0, 0, 0)])
        origin_visited = {(0, 0): 0}

        target_queue = deque([(x, y, 0)])
        target_visited = {(x, y): 0}

        while True:
            or_, oc, os = origin_queue.popleft()
            if (or_, oc) in target_visited:
                return os + target_visited[(or_, oc)]

            tr, tc, ts = target_queue.popleft()
            if (tr, tc) in origin_visited:
                return ts + origin_visited[(tr, tc)]

            origin_neighbors = [(or_ + dr, oc + dc) for dr, dc in offsets]
            target_neighbors = [(tr + dr, tc + dc) for dr, dc in offsets]

            for nr, nc in origin_neighbors:
                if (nr, nc) not in origin_visited:
                    origin_queue.append((nr, nc, os + 1))
                    origin_visited[(nr, nc)] = os + 1

            for nr, nc in target_neighbors:
                if (nr, nc) not in target_visited:
                    target_queue.append((nr, nc, ts + 1))
                    target_visited[(nr, nc)] = ts + 1

        