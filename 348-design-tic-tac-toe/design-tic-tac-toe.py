class TicTacToe:

    def __init__(self, n: int):
        self.board =[ [0 for _ in range(n)] for _ in range(n)]
        self.n = n
        
    # def isWinner(self, player:int ) -> bool:
        
    def move(self, row: int, col: int, player: int) -> int:
        p = 1 if player == 1 else -1
        self.board[row][col] = p

        isDiagonal = 0
        isAntiDiag = 0

        isHorizonal = sum(self.board[row])
        isVertical = sum([self.board[i][col] for i in range(len(self.board))])
        if row == col:
            isDiagonal =sum([self.board[i][i] for i in range(len(self.board))])
        if row+col == self.n - 1:
            isAntiDiag =sum([self.board[i][self.n-i-1] for i in range(len(self.board))])
        
        if abs(isHorizonal) == self.n  or abs(isVertical) == self.n  or abs(isAntiDiag)==self.n or abs(isDiagonal)==self.n:
            return player
        return 0

        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)