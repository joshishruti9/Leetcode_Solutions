class Solution:
    def find_new_land_count(self, queue, visited, m, n, grid):
        
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        count = 0
        
        while queue:
            queue2 = []
            for i, j in queue:
                for di, dj in dirs:
                    if 0 <= i+di < m and 0 <= j+dj < n and (i+di, j+dj) not in visited:
                        if grid[i+di][j+dj] == 0:
                            queue2.append((i+di, j+dj))
                            visited.add((i+di, j+dj))
                        else: #i found land 2
                            return count
            queue = queue2
            count += 1
        
        return count
                

    def capture_land(self, i, j, queue, visited, m, n, grid):
        
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        
        while queue:
            i, j = queue.popleft()
            for di, dj in dirs:
                if 0 <= i+di < m and 0 <= j+dj < n and grid[i+di][j+dj] == 1 and (i+di, j+dj) not in visited:
                    queue.append((i+di, j+dj))
                    visited.add((i+di, j+dj))

    def shortestBridge(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        queue = deque()
        visited = set()
        land_captured = False
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    visited.add((i, j))
                    self.capture_land(i, j, queue, visited, m, n, grid)
                    land_captured = True
                    break
            if land_captured:
                break


        queue = deque(visited)
        return self.find_new_land_count(queue, visited, m, n, grid)
        