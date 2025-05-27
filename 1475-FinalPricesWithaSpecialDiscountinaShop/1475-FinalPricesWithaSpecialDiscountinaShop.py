# Last updated: 5/27/2025, 1:35:14 PM
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        n = len(prices)
        next_min = []
        flag = False

        for i in range(n-1):
            flag = False
            for j in range(i+1, n):
                if prices[j] <= prices[i]:
                    next_min.append(prices[j])
                    flag = True
                    break
            if not flag:
                next_min.append(0)

        next_min.append(0)

        for i in range(n):
            next_min[i] = prices[i] - next_min[i]

        return next_min    