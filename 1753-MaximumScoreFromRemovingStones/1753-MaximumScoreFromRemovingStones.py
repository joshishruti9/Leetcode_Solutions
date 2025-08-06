# Last updated: 8/6/2025, 1:04:16 PM
from heapq import heappush, heappop
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        max1 = max2 = a
        count = 0

        max_heap = []
        heappush(max_heap, -a)
        heappush(max_heap, -b)
        heappush(max_heap, -c)

        while max1 != 0 and max2 != 0:
            max1 = heappop(max_heap)
            max2 = heappop(max_heap)

            heappush(max_heap, max1+1)
            heappush(max_heap, max2+1)

            count += 1
        
        return count-1