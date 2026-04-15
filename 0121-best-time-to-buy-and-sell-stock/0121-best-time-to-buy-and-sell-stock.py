class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_num = float("inf")
        max_diff = 0

        for i in range(len(prices)):
            if prices[i] < min_num:
                min_num = prices[i]
            
            max_diff = max(prices[i] - min_num, max_diff)

        return max_diff
        