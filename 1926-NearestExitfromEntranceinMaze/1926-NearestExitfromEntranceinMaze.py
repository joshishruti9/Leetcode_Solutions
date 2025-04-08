# Last updated: 4/7/2025, 7:00:10 PM
from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        print(*maze, sep = '\n')
        count = 0
        m = len(maze)
        n = len(maze[0])
        visited = set()
        queue = deque()
        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        queue.append(entrance)
        visited.add((entrance[0],entrance[1]))

        while queue:
            queue2 = deque()
            for i, j in queue:
                if (0 == i or m-1 == i or 0 == j or n-1 == j) and [i,j] != entrance:
                    return count 

                for di, dj in directions:
                    if 0 <= i+di < m and 0 <= j+dj < n and (i+di,j+dj) not in visited and maze[i+di][j+dj] == '.':
                        queue2.append((i+di,j+dj)) 
                        visited.add((i+di,j+dj))
            count += 1
            queue = queue2
        return -1  