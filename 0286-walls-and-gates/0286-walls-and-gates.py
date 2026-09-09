from collections import deque
class Solution:
    def traverse(self, queue, visited, m, n, rooms):
        dirs = [(0,1), (-1,0), (1,0), (0,-1)]
        curr_count = 0

        while queue:
            
            queue2 = []

            for i, j in queue:
                for di, dj in dirs:
                    if 0 <= i+di < m and 0 <= j+dj < n and (i+di, j+dj) not in visited and rooms[i+di][j+dj] > 0:
                        rooms[i+di][j+dj] = curr_count+1
                        queue2.append((i+di, j+dj))
                        visited.add((i+di, j+dj))
            
            curr_count += 1
            queue = queue2
                

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        queue = deque()
        visited = set()

        m = len(rooms)
        n = len(rooms[0])

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i,j))
        
        
        self.traverse(queue, visited, m, n, rooms)