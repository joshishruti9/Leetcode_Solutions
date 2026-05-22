from collections import deque

class Solution:
    def find_neighbours(self, queue, i, j, visited, heights, m, n):
        
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]

        for di, dj in dirs:
            if 0 <= i+di < m and 0 <= j+dj < n and (i+di, j+dj) not in visited and heights[i+di][j+dj] >= heights[i][j]:

                queue.append((i+di,j+dj))
                visited.add((i+di, j+dj))
    
    def traverse(self, heights, queue, visited, m, n):
        
        while queue:
            i, j = queue.popleft()
            self.find_neighbours(queue, i, j, visited, heights, m, n)

        return visited

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        visited = set()
        queue = deque()
        queue2 = deque()
        visited2 = set()
        m = len(heights)
        n = len(heights[0])

        for i in range(n):
            queue.append((m-1, i))
            visited.add((m-1, i))
        
        for i in range(m):
            queue.append((i, n-1))
            visited.add((i, n-1))
        
        atlantic_set = self.traverse(heights, queue, visited, m, n)

        for i in range(n):
            queue2.append((0, i))
            visited2.add((0, i))
        
        for i in range(m):
            queue2.append((i, 0))
            visited2.add((i, 0))

        pacific_set = self.traverse(heights, queue2, visited2, m, n)

        return list(pacific_set & atlantic_set)

        