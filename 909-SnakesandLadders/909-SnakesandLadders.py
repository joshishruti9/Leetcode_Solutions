# Last updated: 5/31/2025, 1:00:55 PM
from collections import deque
class Solution:
    def get_row_col(self, pos, n):
        row =  (pos-1) // n

        col = self.get_col(pos, row, n)

        return (n - row - 1, col)
    
    def get_col(self, pos, row, n):

        if row % 2 == 0:
            if pos % n == 0:
                col = n - 1
            else:
                col = (pos % n) - 1
        else:
            if pos % n == 0:
                col = 0
            else:
                col = n - (pos % n)
        return col

    def traverse(self, board, queue, visited, n):

        while queue:
            curr_pos, step_count = queue.popleft()
            
            if curr_pos == (n * n):
                return step_count

            for dice in range(1, 7):
                next_pos = curr_pos + dice

                if next_pos > (n * n):
                    break

                
                #get row col for dice_val
                row, col = self.get_row_col(next_pos, n)

                if board[row][col] != -1:
                    if board[row][col] not in visited:
                        dest = board[row][col]
                        queue.append((dest, step_count+1))
                        visited.add(dest)
                else:
                    if next_pos not in visited:
                        queue.append((next_pos, step_count+1))
                        visited.add(next_pos)

        return -1                 

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        queue = deque()
        visited = set()
        n = len(board)

        visited.add(1)
        queue.append((1,0))
       
        return self.traverse(board, queue, visited, n)