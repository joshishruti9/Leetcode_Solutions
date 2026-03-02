1class Solution:
2    def valid_rows(self, board):
3
4        visited = set()
5
6        for i in range(9):
7            visited.clear()
8            for j in range(9):
9                if board[i][j] in visited and board[i][j] != '.':
10                    return False
11                visited.add(board[i][j])
12    
13        return True
14    
15
16    def valid_cols(self, board):
17
18        visited = set()
19
20        for i in range(9):
21            visited.clear()
22            for j in range(9):
23                if board[j][i] in visited and board[j][i] != '.':
24                    return False
25                visited.add(board[j][i])
26        
27        return True
28    
29    def valid_box(self, board, row, col):
30
31        visited = set()
32        for i in range(row, row+3):
33            for j in range(col, col+3):
34                if board[i][j] in visited and board[i][j] != '.':
35                    return False
36                visited.add(board[i][j])
37        
38        return True
39
40    def isValidSudoku(self, board: List[List[str]]) -> bool:
41        m = len(board)
42        n = len(board[0])
43
44        res = True
45
46        for i in range(0, 9, 3):
47            for j in range(0, 9, 3):
48                if not self.valid_box(board, i, j):
49                    return False
50
51
52
53        return self.valid_rows(board) and self.valid_cols(board)
54        