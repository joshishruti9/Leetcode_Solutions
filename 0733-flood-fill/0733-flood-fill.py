from collections import deque

class Solution:
    def updateNeighbours(self, image, i, j, color, queue, visited, og_color):
        m = len(image)
        n = len(image[0])

        dirs = [(0,1),(0,-1),(1,0),(-1,0)]

        for di, dj in dirs:
            if 0 <= i+di < m and  0 <= j+dj < n and image[i+di][j+dj] == og_color and (i+di, j+dj) not in visited:
                image[i+di][j+dj] = color
                visited.add((i+di, j+dj))
                queue.append((i+di, j+dj))

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        queue = deque()
        visited = set()

        og_color = image[sr][sc]

        if og_color == color:
            return image

        queue.append((sr, sc))
        visited.add((sr, sc))

        while queue:
            i, j = queue.popleft()
            image[i][j] = color
            self.updateNeighbours(image, i, j, color, queue, visited, og_color)
        
        return image
        