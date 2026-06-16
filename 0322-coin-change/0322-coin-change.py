class Solution:
    def dp(self, coins, curr_amount):
    
        if curr_amount in self.memo:
            return self.memo[curr_amount]
        
        self.memo[curr_amount] = float("inf")
        for i in range(len(coins)):
            if curr_amount >= 0:
                self.memo[curr_amount] = min(self.dp(coins, curr_amount - coins[i]), self.memo[curr_amount])
        
        self.memo[curr_amount] += 1
        return self.memo[curr_amount]
        

    def coinChange(self, coins: List[int], amount: int) -> int:

        coins.sort(reverse = True)
        count = 0
        self.memo = {}

        for coin in coins:
            self.memo[coin] = 1

        if amount == 0:
            return 0
        
        self.dp(coins, amount)

        return self.memo[amount] if self.memo[amount] != float("inf") else -1



        