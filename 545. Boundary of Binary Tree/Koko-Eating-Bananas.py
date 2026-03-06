1import math
2class Solution:
3    def can_finish(self, mid, h, piles):
4        count = 0
5        for i in range(len(piles)):
6            count += math.ceil(piles[i] / mid)
7        
8        return count <= h 
9
10
11    def minEatingSpeed(self, piles: List[int], h: int) -> int:
12
13        low = 1
14        high = max(piles)
15        total = sum(piles)
16        ans = float("inf")
17
18        while low < high:
19            mid = (low + high) // 2
20            if self.can_finish(mid, h, piles):
21                high = mid
22            else:
23                low = mid + 1
24    
25                   
26        return low
27            
28
29
30                