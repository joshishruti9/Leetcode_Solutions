# Last updated: 4/16/2025, 1:27:45 PM
class Solution:
    def dp(self, index):
        if index not in self.memo:
            self.memo[index] = self.dp(index-1)
        
        row = self.memo[index]
        res = [1]
        total = 1

        for i in range(1,len(row)):
            total += row[i]
            res.append(total)
            total -= row[i-1]

        res.append(1)
        return res

    def getRow(self, rowIndex: int) -> List[int]:
        
        self.memo = {}

        self.memo[0] = [1]
        self.memo[1] = [1,1]

        self.dp(rowIndex)
        
        return self.memo[rowIndex]