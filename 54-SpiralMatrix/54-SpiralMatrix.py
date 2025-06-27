# Last updated: 6/27/2025, 1:16:37 AM
class Solution:
    def traverse(self, n, start, mat):
        sr = sc = start
        er = ec = n - 1 - start

        if sr == er:
            mat[sr][er] = self.num
            return mat

        for j in range(sc,ec):
            mat[sr][j] = self.num
            self.num += 1
        
        for i in range(sr,er):
            mat[i][ec] = self.num
            self.num += 1
        
        for j in range(ec, sc,-1):
            mat[er][j] = self.num
            self.num += 1
        
        for i in range(er,sr,-1):
            mat[i][sc] = self.num
            self.num += 1
        

    def generateMatrix(self, n: int) -> List[List[int]]:
        spiral_count = math.ceil(n / 2)
        self.num = 1

        mat = [[0] * n for i in range(n)]

        #calculate spiral count
        for i in range(spiral_count):
            self.traverse(n, i, mat)

        return mat