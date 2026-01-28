class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # directions = [(0,1),(-1,0),(-1,0),(1,0)]

        m = len(board)
        n = len(board[0])

        visited = set()


        def bactrack(r, c, word):

            if not word:
                return True

            if r < 0 or r >= m or c < 0 or c >= n or board[r][c]!=word[0] or (r,c) in visited:
                return False
            
            visited.add((r,c))

            found = bactrack(r+1, c, word[1:]) or bactrack(r, c-1, word[1:]) \
                    or bactrack(r-1, c, word[1:]) or bactrack(r, c+1, word[1:])
            
            visited.remove((r,c))
            return found
        
        # we dont know the starting pt of the word
        #  We need to start DFS from each pt

        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0] and (r,c) not in visited:
                    # if found below
                    if bactrack(r,c, word):
                        return True
        return False


        

        m = len(board)
        n = len(board[0])

        visited = set()

        # method II
        def dfs(r, c, word):
            if not word:
                return True

            if 0 >r  or r >= m or 0 > c  or c >= n or (r,c) in visited or word[0] != board[r][c]:
                return False
        
            visited.add((r, c))

            found = False
            for nr, nc in [(r+1,c), (r-1,c), (r,c-1), (r,c+1)]:
                found = dfs(nr, nc, word[1:]) 
                if found: # dont overwrite True
                    break
            visited.remove((r, c))
            return found

        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0] and (r, c) not in visited:
                    if dfs(r, c, word):
                        return True
        return False

        
        
        

