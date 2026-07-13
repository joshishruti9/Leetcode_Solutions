class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        first_buy = float('-inf')
        fisrt_sell = 0
        second_buy = float('-inf')
        second_sell = 0

        for price in prices:
            first_buy = max(first_buy, -price)
            fisrt_sell = max(fisrt_sell, first_buy + price)

            second_buy = max(second_buy, fisrt_sell - price)
            second_sell = max(second_sell, second_buy + price)

        return second_sell