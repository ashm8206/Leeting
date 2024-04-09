class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:

        m = len(board)
        n = len(board[0])

        while True:
            stable = True
            crushable = set()
            # horizontal candies
            for r in range(m):
                for c in range(n-2):
                    if board[r][c] == board[r][c+1] == board[r][c+2] != 0:
                        stable = False
                        # only horizontal or vertical. Not both at the same time
                        crushable.update([(r,c),(r,c+1),(r,c+2)]) 

            # vertical candies
            for c in range(n):
                for r in range(m-2):
                    if board[r][c] == board[r+1][c] == board[r+2][c] != 0:
                        stable = False
                        # only horizontal or vertical. Not both at the same time
                        crushable.update([(r,c),(r+1,c),(r+2,c)])

            if stable:
                return board 
            
            for r,c in crushable:
                board[r][c]=0

            # let candies fall
            for c in range(n):
                lowestZero = m -1

                for r in range(m-1,-1,-1):
                    if board[r][c]==0:
                        lowestZero = r
                        break

                # lowestZero = -1

                # for r in range(m-1,-1,-1):
                #     if board[r][c]==0:
                #         lowestZero = max(lowestZero,r)
                #     elif lowestZero >= 0:
                #         board[r][c], board[lowestZero][c] = board[lowestZero][c], board[r][c]
                #         lowestZero -= 1

                # move zeroes based on lowest Non-Zero Index
                for runner in range(lowestZero, -1,-1):
                    if board[runner][c]!=0:
                        # put the nonzero value at lowestZero Position
                        # Put Zero at the NonZero value position
                        board[lowestZero][c],board[runner][c] = board[runner][c],board[lowestZero][c]
                        lowestZero-=1
                # print(board)
            
                    


        




    