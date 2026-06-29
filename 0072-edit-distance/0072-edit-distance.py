class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        m = len(word1)
        n = len(word2)

        mat = [[0 for i in range(n+1)] for j in range(m+1)]

        count = 1
        for i in range(m-1, -1, -1):
            mat[i][n] = count
            count += 1
        count = 1

        for j in range(n-1, -1, -1):
            mat[m][j] = count
            count += 1
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if word1[i] == word2[j]:
                    mat[i][j] = mat[i+1][j+1]
                else:
                    mat[i][j] = 1 + min(mat[i+1][j], mat[i][j+1], mat[i+1][j+1])
        
        return mat[0][0]