# Last updated: 7/2/2025, 12:52:46 PM
from heapq import heappush, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for num in nums:
            if len(min_heap) < k:
                heappush(min_heap,num)
            else:
                temp = heappop(min_heap)
                if num > temp:
                    heappush(min_heap,num)
                else:
                    heappush(min_heap,temp)
        
        return heappop(min_heap)