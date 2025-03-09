from collections import deque
class Solution:
    def add_neighbours(self, image, i, j, queue, m, n, orginal_color):
        
        indexes = [(-1,0),(1,0),(0,-1),(0,1)]
        for di, dj in indexes:
            if 0 <= i + di < m and 0 <= j + dj < n and image[i+di][j+dj] == orginal_color:
                queue.append((di+i,dj+j))

    def traverse(self,image,sr,sc,color):
        m = len(image)
        n = len(image[0])
        queue = deque()
        queue.append((sr, sc))
        orginal_color = image[sr][sc]

        while queue:
            i , j = queue.popleft()
            self.add_neighbours(image, i, j, queue, m, n, orginal_color)
            image[i][j] = color


    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if color == image[sr][sc]:
            return image

        self.traverse(image, sr, sc, color)

        return image
        