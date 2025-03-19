class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        for i in range(len(prices)):
            if prices[i] > min_price:
                max_profit += (prices[i] - min_price)
                min_price = prices[i]
            elif prices[i] < min_price:
                min_price = prices[i]
        return max_profit