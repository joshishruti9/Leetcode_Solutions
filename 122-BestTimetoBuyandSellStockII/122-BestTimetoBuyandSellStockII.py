# Last updated: 7/11/2025, 3:55:27 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float("inf")

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit += price - min_price
                min_price = price

        return max_profit