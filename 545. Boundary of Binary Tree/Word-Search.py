1class Solution:
2    def find_neighbours(self, visited, i, j, m, n, board, word, index):
3
4
5        dirs = [(-1,0),(0,-1),(1,0),(0,1)]
6
7        if index == len(word):
8            return True
9
10        for di, dj in dirs:
11            if 0 <= i+di < m and 0 <= j+dj < n and (i+di, j+dj) not in visited and board[i+di][j+dj] == word[index]:
12                visited.add((i+di,j+dj))
13                if self.find_neighbours(visited, i+di, j+dj, m, n, board, word, index+1):
14                    return True
15                visited.remove((i+di,j+dj))
16        
17        return False
18
19    def exist(self, board: List[List[str]], word: str) -> bool:
20        m = len(board)
21        n = len(board[0])
22        queue = deque()
23        visited = set()
24        ans = False
25
26        for i in range(m):
27            for j in range(n):
28                if board[i][j] == word[0]:
29                    visited.add((i,j))
30                    if self.find_neighbours(visited, i, j, m, n, board, word, 1):
31                        return True
32                    
33                    visited.clear()
34                    
35        
36        return False
37            
38
39
40        