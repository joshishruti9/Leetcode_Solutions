# Last updated: 3/29/2025, 4:38:34 PM
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        max_stack = []
        discount_map = dict()
        result = prices

        for i in range(len(prices)):
            while max_stack and prices[max_stack[-1]] >= prices[i]:
                item = max_stack.pop()
                result[item] = (prices[item] - prices[i])
            max_stack.append(i)
        return result