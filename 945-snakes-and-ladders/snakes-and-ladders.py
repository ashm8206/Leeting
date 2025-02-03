class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        n = len(board)

        def label_to_position(position):
            r, c = divmod(position-1, n)
            if r%2==0:
                return n-r-1, c
            else:
                return n-r-1, n-c-1
        

        seen = set()
        queue = collections.deque()
        queue.append((1,0))
        seen.add(1)
        while queue:
            label, level = queue.popleft()
            
            r, c = label_to_position(label)
           

            if board[r][c]!=-1:
                label = board[r][c]
                

            if label== n*n:
                return level
            
            for x in range(1, 7):
                new_label = label + x
                if new_label not in seen and new_label <= n*n:
                    seen.add(new_label)
                    queue.append((new_label, level+1))
        return -1