# Last updated: 7/9/2025, 5:48:54 PM
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
            mul = mul * num
        
        return mul % (10 ** 9 + 7)