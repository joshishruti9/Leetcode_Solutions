1class Solution:
2    def orangesRotting(self, grid: List[List[int]]) -> int:
3        queue = deque()
4        m = len(grid)
5        n = len(grid[0])
6
7        queue = deque()
8        visited = set()
9
10        self.count = 0
11
12
13        for i in range(m):
14            for j in range(n):
15                if grid[i][j] == 2:
16                    queue.append((i,j))
17                    visited.add((i,j))
18
19
20        while queue:
21            
22            queue2 = []
23            for i, j in queue:
24                dirs = [(0,1),(1,0),(-1,0),(0,-1)]
25                for di, dj in dirs:
26                    if 0 <= i+di < m and 0 <= j+dj < n and (i+di,j+dj) not in visited and grid[i+di][j+dj] == 1:
27                        queue2.append((i+di, j+dj))
28                        visited.add((i+di, j+dj))
29                        grid[i+di][j+dj] = 2
30           
31            if queue2:
32                self.count += 1
33            queue = queue2
34
35
36        for i in range(m):
37            for j in range(n):
38
39                if grid[i][j] == 1:
40                    return -1
41
42
43        return self.count 
44
45        