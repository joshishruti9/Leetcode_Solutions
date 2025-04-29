# Last updated: 4/28/2025, 10:46:42 PM
class Solution:
    def dp(self, coins, amount):
        if amount not in self.memo:
            self.memo[amount] = float('inf')
            for coin in coins:
                rem_coin = amount - coin
                if rem_coin < 0:
                    continue
                self.memo[amount] = min(self.dp(coins, rem_coin), self.memo[amount])
            self.memo[amount] += 1
        return self.memo[amount]

    def coinChange(self, coins: List[int], amount: int) -> int:
        self.memo = dict()

        self.memo[0] = 0
        
        if amount == 0:
            return 0

        self.dp(coins, amount)
        if self.memo[amount] == float('inf'):
            return -1
        return self.memo[amount]
        