# Last updated: 4/15/2025, 1:31:25 PM
class Solution:
    def dp(self, i, j):
        if (i,j) not in self.memo:
            self.memo[(i,j)] = self.dp(i+1,j) + self.dp(i,j+1)
        
        return self.memo[(i,j)]
    def uniquePaths(self, m: int, n: int) -> int:

        self.memo = {}

        for i in range(n):
            self.memo[(m-1,i)] = 1
        
        for i in range(m):
            self.memo[(i,n-1)] = 1
        
        self.dp(0,0)
        
        return self.memo[(0,0)] 