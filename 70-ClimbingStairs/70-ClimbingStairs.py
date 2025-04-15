# Last updated: 4/14/2025, 9:56:11 PM
class Solution:
    def dp(self, k):
        if k not in self.memo:
            self.memo[k] = self.dp(k-1) + self.dp(k-2)
        
        return self.memo[k]

    def climbStairs(self, n: int) -> int:
        self.memo = {}
        
        self.memo[1] = 1
        self.memo[2] = 2

        count = self.dp(n)
        return self.memo[n]