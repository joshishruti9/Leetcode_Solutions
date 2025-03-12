from heapq import heappush, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        min_heap = []
        for num in nums:
            if len(min_heap) < k:
                heappush(min_heap,num)
            else:
                number = heappop(min_heap)
                if num > number:
                    heappush(min_heap,num)
                elif num == number:
                    heappush(min_heap,num)
                else:
                    heappush(min_heap,number)

        return min_heap[0]       