class Solution:
    def dp(self, n):
        if n in self.memo:
            return self.memo[n]
        
        total_count = self.dp(n-1) + self.dp(n-2)
        self.memo[n] = total_count
        return self.memo[n]

    def climbStairs(self, n: int) -> int:
        self.memo = {}

        self.memo[1] = 1
        self.memo[2] = 2

        return self.dp(n)
        