1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3
4        min_price = prices[0]
5        max_diff = 0
6
7        for i in range(1,len(prices)):
8            if prices[i] < min_price:
9                min_price = prices[i]
10            
11            max_diff = max(max_diff, prices[i]-min_price)
12        
13        return max_diff
14
15
16        