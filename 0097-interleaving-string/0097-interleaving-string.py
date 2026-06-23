class Solution:
    def backtrack(self, curr_s1, curr_s2, curr_s3, s1, s2, s3):

        if (curr_s1, curr_s2, curr_s3) in self.memo:
            return self.memo[(curr_s1, curr_s2, curr_s3)]

        if curr_s1 == len(s1) and curr_s2 == len(s2) and curr_s3 == len(s3):
            self.memo[(curr_s1, curr_s2, curr_s3)] = True
            return True
        
        if curr_s1 < len(s1) and s1[curr_s1] == s3[curr_s3]:
            if self.backtrack(curr_s1+1, curr_s2, curr_s3+1, s1, s2, s3):
                self.memo[(curr_s1, curr_s2, curr_s3)] = True
                return True
          
        if curr_s2 < len(s2) and  s2[curr_s2] == s3[curr_s3]:
            if self.backtrack(curr_s1, curr_s2+1, curr_s3+1, s1, s2, s3):
                self.memo[(curr_s1, curr_s2, curr_s3)] = True
                return True
            
        self.memo[(curr_s1, curr_s2, curr_s3)] = False
        
        return self.memo[(curr_s1, curr_s2, curr_s3)]
        

    

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        self.memo = {}
        
        self.backtrack(0, 0, 0, s1, s2, s3)

        return self.memo[(0, 0, 0)]


        