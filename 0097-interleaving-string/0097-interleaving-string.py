class Solution:
    def backtrack(self, s1, s2, s3, i, j):
        if (i, j) in self.memo:
            return self.memo[(i, j)]

        k = i + j
        if i == len(s1) and j == len(s2) and k == len(s3):
            self.memo[(i, j)] = True
            return True
        
        if (i < len(s1) and k < len(s3) and s1[i] != s3[k]) and (j < len(s2) and k < len(s3) and s2[j] != s3[k]):
            self.memo[(i, j)] = False
            return False
        
        s1_res = s2_res = False

        if i < len(s1) and k < len(s3) and s1[i] == s3[k]:
            s1_res = self.backtrack(s1, s2, s3, i+1, j)
        
        if j < len(s2) and k < len(s3) and s2[j] == s3[k]:
            s2_res = self.backtrack(s1, s2, s3, i, j+1)
        
        self.memo[(i, j)] = s1_res or s2_res
        
        return self.memo[(i, j)]


    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
            
        self.memo = {}
        self.backtrack(s1, s2, s3, 0, 0)
        return self.memo[(0 ,0)]
        