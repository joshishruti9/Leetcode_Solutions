from collections import deque

class Solution:
    def update_cell(self, board, update_list):

        for i, j in update_list:
            board[i][j] = 'X'

    def traverse(self, board, queue, visited, m, n):
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        update_list = []
        flag = True

        while queue:
            i, j = queue.popleft()
            update_list.append((i,j))
            for di, dj in dirs:
                if 0 < i+di < m-1 and 0 < j+dj < n-1 and board[i+di][j+dj] == 'O' and (i+di, j+dj) not in visited:
                    queue.append((i+di, j+dj))
                    visited.add((i+di, j+dj))
                elif (i+di == 0 or i+di == m-1 or j+dj == 0 or j+dj == n-1) and board[i+di][j+dj] == 'O':
                    flag = False
        
        if flag:
            self.update_cell(board, update_list)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        queue = deque()
        visited = set()

        m = len(board)
        n = len(board[0])

        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == 'O' and (i,j) not in visited:
                    queue.append((i,j))
                    visited.add((i,j))
                    self.traverse(board, queue, visited, m, n)

        