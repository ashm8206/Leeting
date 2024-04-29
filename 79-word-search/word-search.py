class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # directions = [(0,1),(-1,0),(-1,0),(1,0)]

        m = len(board)
        n = len(board[0])

        visited = set()
        
        def bactrack(r,c, k):

            if k == len(word):
                return True
    
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c]!=word[k] or (r,c) in visited:
                return False
            
            visited.add((r,c))

            ans = bactrack(r+1, c, k+1) or bactrack(r, c-1, k+1) \
                    or bactrack(r-1, c, k+1) or bactrack(r, c+1, k+1)
            
            visited.remove((r,c))

            return ans
        
        # we dont know the starting pt of the word
        #  We need to start DFS from each pt

        for r in range(m):
            for c in range(n):
                if bactrack(r,c, 0):
                    return True
        return False

