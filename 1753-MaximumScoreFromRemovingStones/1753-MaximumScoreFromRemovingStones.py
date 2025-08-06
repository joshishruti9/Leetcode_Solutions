# Last updated: 8/6/2025, 1:13:16 PM
from heapq import heappush, heappop
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        max1 = max2 = a
        count = 0

        max_heap = []
        heappush(max_heap, -a)
        heappush(max_heap, -b)
        heappush(max_heap, -c)

        while True:
            max1 = -heappop(max_heap)
            max2 = -heappop(max_heap)

            print(max1, " ", max2)

            if max1 == 0 or max2 == 0:
                break

            count += 1
            heappush(max_heap, -(max1-1))
            heappush(max_heap, -(max2-1))

               
        return count