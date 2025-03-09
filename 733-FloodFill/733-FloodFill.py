from collections import deque
class Solution:
    def add_neighbours(self, image, i, j, queue, m, n, orginal_color):
        
        if 0 <= i+1 < m and image[i+1][j] == orginal_color:
            queue.append((i+1,j))
        
        if 0 <= j+1 < n and image[i][j+1] == orginal_color:
            queue.append((i,j+1))
           
        if 0 <= i-1 < m and image[i-1][j] == orginal_color:
            queue.append((i-1,j))
        
        if 0 <= j-1 < n and image[i][j-1] == orginal_color:
            queue.append((i,j-1))

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
        