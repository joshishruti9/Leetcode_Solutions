class Solution:
    def countServers(self, grid: List[List[int]]) -> int:

        row_len = len(grid)
        col_len = len(grid[0])

        count = 0
        visited_row = [0] * row_len
        visited_col = [0] * col_len

        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == 1:
                    visited_row[i] += 1
                    visited_col[j] += 1
            
        for i in range(col_len):
            for j in range(row_len):
                if grid[j][i] == 1 and (visited_row[j] > 1 or visited_col[i] > 1):
                    count += 1
            
           
        return count