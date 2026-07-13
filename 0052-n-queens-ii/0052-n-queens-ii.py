class Solution:
    def isSafe(self, board, row, col, n):

        r = row
        c = col
       
        while c >= 0:
            if board[r][c-1] == "Q":
                return False
            c -= 1
        
        r = row
        c = col
        while r < n-1 and c >= 0:
            if board[r+1][c-1] == "Q":
                return False
            r += 1
            c -= 1
        
        r = row
        c = col
        while r > 0 and c >= 0:
            if board[r-1][c-1] == "Q":
                return False
            r -= 1
            c -= 1
       
        return True

    def solve(self, board, col, n):
        if col == n:
            self.count += 1
            return

        for row in range(n):
            if self.isSafe(board, row, col, n):
                board[row][col] = "Q"
                self.solve(board, col+1, n)
                board[row][col] = "."

    def totalNQueens(self, n: int) -> int:

        board = [['.' for j in range(n)] for i in range(n)]
        self.count = 0

        self.solve(board, 0, n)

        return self.count