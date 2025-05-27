# Last updated: 5/27/2025, 1:34:19 PM
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        n = len(prices)
        answer = [0 for i in range(n)]
        min_latest = 1001
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
            answer[i] = prices[i] - next_min[i]

        return answer
                
            
        