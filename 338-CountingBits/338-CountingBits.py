# Last updated: 4/16/2025, 1:45:11 PM
class Solution:
    def count_one(self, n, count):
        if n == 0:
            return count
        if n % 2 == 1:
            count += 1
        n = n // 2
        return self.count_one(n,count)

    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(0,n+1):
            count = self.count_one(i, 0)
            res.append(count)
            
        return res