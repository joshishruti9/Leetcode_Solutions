from collections import deque
class Solution:
    def capture_region(self,board,validIsland):
        print("Hello")
        print(validIsland)
        for i, j in validIsland:
            board[i][j] = "X"
        
    
    def getNeighbours(self,board,i,j,m,n,queue,visited,validIsland):
        
        directions = {(1,0),(-1,0),(0,1),(0,-1)}
        flag = True
        for di,dj in directions:
            if 1 <= i+di < m-1 and 1 <= j+dj < n-1 and board[i+di][j+dj] == 'O':
                queue.append((i+di,j+dj))
                visited.add((i+di,j+dj))
                validIsland.append((i+di,j+dj))
                flag = True
            if i+di == 0 or i+di == m-1 or j+dj == 0 or j+dj == n-1:
                flag = False
        print("flag:",flag)
        return flag
    
    def find_region(self, board,m,n, queue, visited):
        flag = True
        validIsland = []
        directions = {(1,0),(-1,0),(0,1),(0,-1)}
        while queue:
            i , j = queue.popleft()
            validIsland.append((i,j))
            for di,dj in directions:
                if 1 <= i+di < m-1 and 1 <= j+dj < n-1 and board[i+di][j+dj] == 'O' and (i+di,j+dj) not in visited:
                    queue.append((i+di,j+dj))
                    visited.add((i+di,j+dj))
                elif (i+di == 0 or i+di == m-1 or j+dj == 0 or j+dj == n-1) and board[i+di][j+dj] == 'O':
                    flag = False
        print(flag)
        if flag:
            self.capture_region(board,validIsland)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        queue = deque()
        visited = set()

        for i in range(1,m-1):
            for j in range(1,n-1):
                if board[i][j] == 'O' and (i,j) not in visited:
                    queue.append((i,j))
                    visited.add((i,j))
                    self.find_region(board,m,n,queue,visited)    