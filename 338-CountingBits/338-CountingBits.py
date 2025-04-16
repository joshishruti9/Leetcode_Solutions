# Last updated: 4/16/2025, 1:56:12 PM
class Solution:
    def dp(self, n):
        count = 0
        if n not in self.memo:
            if n % 2 == 1:
                count = 1
            num = n >> 1
            self.memo[n] = count + self.dp(num)

        return self.memo[n]
    

    def countBits(self, n: int) -> List[int]:
        self.memo = {}
        res = []

        self.memo[0] = 0
        self.memo[1] = 1

        for i in range(0,n+1):
            ans = self.dp(i)
            res.append(ans)

        return res