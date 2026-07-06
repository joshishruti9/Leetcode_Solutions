class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        m = len(image)
        n = len(image[0])

        res = [[0 for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                res[i][j] = 1 - image[i][n-1-j]
        
        return res