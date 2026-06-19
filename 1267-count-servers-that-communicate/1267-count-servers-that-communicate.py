class Solution:
    def countServers(self, grid: List[List[int]]) -> int:

        row_len = len(grid)
        col_len = len(grid[0])

        communicating_servers = set()

        for i in range(row_len):
            visited = set()
            for j in range(col_len):
                if grid[i][j] == 1:
                    visited.add((i, j))
            
            if len(visited) > 1:
                communicating_servers.update(visited)


        for i in range(col_len):
            visited = set()
            for j in range(row_len):
                if grid[j][i] == 1:
                    visited.add((j, i))
            
            if len(visited) > 1:
                communicating_servers.update(visited)
        
        return len(communicating_servers)