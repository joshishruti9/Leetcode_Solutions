# Last updated: 7/9/2025, 5:50:32 PM
from heapq import heappush, heappop
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        min_heap = []

        for num in nums:
            heappush(min_heap, num)
        
        while k > 0:
            num = heappop(min_heap)
            heappush(min_heap, num+1)
            k -= 1
        
        mul = 1

        for num in min_heap:
            mul = (mul * num) % (10 ** 9 + 7)
        
        return mul