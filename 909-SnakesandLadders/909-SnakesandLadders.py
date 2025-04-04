# Last updated: 4/3/2025, 11:11:04 PM
from collections import deque
from math import ceil

class Solution:
    def get_row_col(self, n, value):
        pos_ceil = ceil(value / n)
        r = n - pos_ceil
        if (pos_ceil % 2) == 1:
            c = (value - 1) % n
        else:
            c = pos_ceil * n - value
        return r,c

         
    def traverse(self, board, start, end, n, queue, visited):
        while queue:
            node, steps = queue.popleft()
            if node == end:
                return steps

            for i in range(1,7):
                pos = node + i
                if pos > (n * n):
                    break
                r,c = self.get_row_col(n,pos)
                if board[r][c] != -1:
                    pos = board[r][c]
                    r, c = self.get_row_col(n, pos)
                    if pos not in visited:
                        visited.add(pos)
                        queue.append((pos, steps+1))
                else:
                    if pos not in visited:
                        visited.add(pos)
                        queue.append((pos, steps+1))
        return -1

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        visited = set()
        queue = deque()

        n = len(board)

        start = 1
        end = n * n
        queue.append((1,0))
        visited.add(1)
        return self.traverse(board,start, end, n, queue, visited)