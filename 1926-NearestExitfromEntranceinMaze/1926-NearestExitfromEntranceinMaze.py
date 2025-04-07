# Last updated: 4/7/2025, 2:19:58 PM
from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        visited = set()
        queue = deque()
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        x, y = entrance

        queue.append((x, y, 0))
        visited.add((x,y))

        while queue:
            i, j, count = queue.popleft()

            for di, dj in directions:
                if 0 <= i+di < m and 0 <= j+dj < n and (i+di,j+dj) not in visited and maze[i+di][j+dj] == '.':
                    if (0 == i+di or m-1 == i+di) or (0 == j+dj or n-1 == j+dj):
                        return count + 1
                    queue.append((i+di,j+dj, count+1)) 
                    visited.add((i+di,j+dj))
          
        return -1  