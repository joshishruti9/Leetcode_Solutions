from collections import deque

class Solution:
    def find_col(self, pos, n, row_num):
        if row_num % 2 != 0:
            if pos % n == 0:
                col = 0
            else:
                col = n - (pos % n)
        else:
            if pos % n == 0:
                col = n-1
            else:
                col = (pos % n) - 1        

        return col


    def find_row(self, pos, n):
        if pos % n == 0:
            return ((pos-1) // n)
        else:
            return (pos // n)

    def traverse(self, board, queue, visited, n):

        step_count = 0

        while queue:
            queue2 = []
            
            for curr_pos in queue:

                for i in range(1,7):
                    next_pos = curr_pos + i

                    if next_pos > (n * n):
                        break
                    
                    row = self.find_row(next_pos, n)
                    col = self.find_col(next_pos, n , row)

                    dest = next_pos

                    if board[n-1-row][col] != -1:
                        dest = board[n-1-row][col]

                    if dest == (n * n):
                        return step_count + 1

                    if dest not in visited:
                        visited.add(dest)
                        queue2.append(dest)
            
            step_count += 1
            queue = queue2
          
            
        return -1

    def snakesAndLadders(self, board: List[List[int]]) -> int:

        queue = deque()
        visited = set()
        queue.append(1)
        visited.add(1)

        return self.traverse(board, queue, visited, len(board))
        