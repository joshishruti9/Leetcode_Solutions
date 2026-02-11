1from collections import deque
2class Solution:
3    def find_neighbours(self,rooms, i, j, m, n, visited, queue2, count):
4        dirs = [(-1,0),(0,-1),(1,0),(0,1)]
5
6        for di, dj in dirs:
7            if 0 <= i+di < m and 0 <= j+dj < n and rooms[i+di][j+dj] != -1 and (i+di,j+dj) not in visited:
8                queue2.append((i+di, j+dj))
9                visited.add((i+di, j+dj))
10                rooms[i+di][j+dj] = count
11
12    def wallsAndGates(self, rooms: List[List[int]]) -> None:
13        """
14        Do not return anything, modify rooms in-place instead.
15        """
16        m = len(rooms)
17        n = len(rooms[0])
18
19        queue = deque()
20        visited = set()
21        count = 1
22
23        for i in range(m):
24            for j in range(n):
25                if rooms[i][j] == 0:
26                    queue.append((i,j))
27                    visited.add((i,j))
28
29
30        while queue:
31            queue2 = []
32
33            for i, j in queue:
34                self.find_neighbours(rooms, i, j, m, n, visited, queue2, count)
35
36            queue = queue2
37            count += 1
38        