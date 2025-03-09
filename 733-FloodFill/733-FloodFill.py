from collections import deque
class Solution:
    def add_neighbours(self, image, i, j, queue, visited, m, n, orginal_color):
        
        if 0 <= i+1 < m and (i+1,j) not in visited and image[i+1][j] == orginal_color:
            queue.append((i+1,j))
            visited.add((i+1,j))
        
        if 0 <= j+1 < n and (i,j+1) not in visited and image[i][j+1] == orginal_color:
            queue.append((i,j+1))
            visited.add((i,j+1))
        
        if 0 <= i-1 < m and (i-1,j) not in visited and image[i-1][j] == orginal_color:
            queue.append((i-1,j))
            visited.add((i-1,j))
        
        if 0 <= j-1 < n and (i,j-1) not in visited and image[i][j-1] == orginal_color:
            queue.append((i,j-1))
            visited.add((i,j-1))

    def traverse(self,image,sr,sc,color):
        m = len(image)
        n = len(image[0])
        queue = deque()
        visited = set()
        queue.append((sr, sc))
        visited.add((sr, sc))
        orginal_color = image[sr][sc]

        while queue:
            i , j = queue.popleft()
            self.add_neighbours(image, i, j, queue, visited, m, n, orginal_color)
            image[i][j] = color


    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.traverse(image, sr, sc, color)

        return image
        