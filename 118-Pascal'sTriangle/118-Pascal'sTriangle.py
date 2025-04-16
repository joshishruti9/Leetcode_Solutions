# Last updated: 4/16/2025, 12:52:49 PM
class Solution:
    def dp(self, numsRows):
        if numsRows not in self.memo:
            self.memo[numsRows] = self.dp(numsRows-1)
        
        res = [] 
        last_row = self.memo[numsRows]
        total = 1
        res.append(1)

        for i in range(1,len(last_row)):
            total += last_row[i]
            res.append(total)
            total -= last_row[i-1]
        res.append(1)
        return res
            

    def generate(self, numRows: int) -> List[List[int]]:
        self.memo = {}
        res = []

        self.memo[1] = [1]
        self.memo[2] = [1,1]

        self.dp(numRows)
        
        for i in range(1,numRows+1):
            res.append(self.memo[i])

        return res
