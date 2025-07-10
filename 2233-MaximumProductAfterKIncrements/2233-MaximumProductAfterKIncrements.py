# Last updated: 7/9/2025, 5:42:46 PM
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

        while min_heap:
            mul = mul * heappop(min_heap)
        
        return mul % (10 ** 9 + 7)