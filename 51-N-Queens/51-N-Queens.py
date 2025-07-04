# Last updated: 7/3/2025, 7:43:26 PM
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
        
        r = row
        c = col
        while r < n-1 and c >= 0:
            if board[r+1][c-1] == "Q":
                return False
            r += 1
            c -= 1
       
        return True

    def solve(self, board, col, n, ans):
        if col == n:
            ans.append(["".join(col) for col in board])
            return

        for row in range(n):
            if self.isSafe(board, row, col, n):
                board[row][col] = "Q"
                self.solve(board, col+1, n, ans)
                board[row][col] = "."

    def solveNQueens(self, n: int) -> List[List[str]]:
        
        board = [['.' for j in range(n)] for i in range(n)]
        ans = []

        self.solve(board, 0, n, ans)

        return ans